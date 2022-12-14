#!/usr/bin/python3
import aocd
from collections import deque
import re
import sys

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


class Inventory:
  def __init__(self, name):
    self.inv = [0 for _ in [ORE, CLAY, OBSIDIAN, GEODE]]
    self.name = name

  def __repr__(self):
    return f'<Inventory {self.name} {self.inv}>'

  def get(self, i):
    return self.inv[i]

  def set(self, i, v):
    self.inv[i] = v
    return self.inv[i]

  def incr(self, i, v=1):
    self.inv[i] += v
    return self.inv[i]

  def sub(self, i, v):
    return self.incr(i, v * -1)

  def ore(self):
    return self.inv[ORE]


class Blueprint:
  def __init__(self, line):
    self._name = {'ore': ORE, 'clay': CLAY, 'obsidian': OBSIDIAN, 'geode': GEODE}
    self._item = {}
    for k, v in self._name.items():
      self._item[v] = k
    line = line.strip()
    line = line.replace(".", "")
    p = line.split("Each ")
    m = re.match("Blueprint (\\d+): ", p[0])
    self.number = m.group(1)
    self.bp = {}
    for e in p[1:]:
      m = re.match("(.*) robot costs (.*)", e)
      if not m:
        print(e)
        exit(1)
      robot = self._name[m.group(1)]
      cost = {}
      for item in m.group(2).strip().split(" and "):
        (count, name) = item.split(" ")
        name = self._name[name]
        cost[name] = int(count)
      self.bp[robot] = cost

  def __repr__(self):
    return f'<Blueprint {self.number} {self.bp}>'


def main(test):
  mod = aocd.models.Puzzle(year=2022, day=19)
  if not test:
    data = mod.input_data
  else:
    data = ""
    for line in mod.example_data.splitlines():
      if not line:
        data += "\n\n"
      else:
        data += line + " "
  bp = []
  for line in data.split("\n\n"):
    bp.append(Blueprint(line))
  print(bp)
  mat = Inventory("material")
  robot = Inventory("robot")
  robot.incr(ORE)
  print(mat, robot)

  b = bp[0]

  q = deque()

  t = 1
  while t<=24:
    nr = []
    pos = []
    for r, ri in b.bp.items():
      build = True
      for i in ri:
        if mat.get(i) < ri[i]:
          build = False
          break
      if build and robot.get(r) < 2 or min(robot.inv) > 0:
        pos.append(r)

    if pos:
      pos.reverse()
      print(f'possible: {pos}')
      r = pos[0]
      ri = b.bp[r]
      print(f'build {r} robot with {ri}')
      for i in ri:
        mat.sub(i, ri[i])
      nr.append(r)
    for r, c in enumerate(robot.inv):
      mat.incr(r, c)
    if pos:
      for r in nr:
        robot.incr(r)
    print(f'end of {t}: {mat} {robot}')
    t+=1


if __name__ == '__main__':
  main(len(sys.argv) > 1)
