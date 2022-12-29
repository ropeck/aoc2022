#!/usr/bin/python3
import sys

def compare(l, r, d=0):
  print(" "*d + "compare",l, r)
  if not type(l) == list:
    l = [l]
  if not type(r) == list:
    r = [r]
  for a,b in zip(l, r):
    if type(a) == int and type(b) == int:
      print(" " * (d+2), a, b, b-a)
      rec = b - a
    else:
      rec = compare(a, b, d+2)
    print(" "*d + "rec", rec)
    if rec:
      return rec
  print("equal", len(r) - len(l))
  return len(r) - len(l)

def main(path):
  signals = []
  with open(path, "r") as fh:
    while True:
      a = fh.readline()
      if not a:
        break
      b = fh.readline()
      _ = fh.readline()
      signals.append((eval(a),eval(b)))

  sum = 0
  for i, (l, r) in enumerate(signals):
    if compare(l, r) > 0:
      sum += (i+1)
      print("ok", i+1)
    print("")

  print("")
  print("total", sum)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
