#!/usr/bin/python3


def range_to_set(r):
  (a, b) = r.split("-")
  return set([n for n in range(int(a), int(b)+1)])

def main():
  total = 0
  for line in open("input","r"):
    (a, b) = line.strip().split(",")
    sa = range_to_set(a)
    sb = range_to_set(b)
    if sa.issubset(sb) or sb.issubset(sa):
      total += 1
  print(f'total: {total}')
if __name__ == '__main__':
  main()
