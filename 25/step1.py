#!/usr/bin/python3
import sys
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def carry(n, i):
  if i < len(n)-1:
    n[i+1] = (n[i+1] + 1) 
    if n[i+1] > 4:
      n[i+1] = n[i+1] % 5
      n = carry(n, i+1)
  else:
    n.append(1)
  return n

def borrow(n, i):
  if i < len(n):
    if str(n[i]) in "-=":
      v = "012-=".index(str(n[i]))
    else:
      v = int(n[i])
    if v == 0:
      n = borrow(n, i+1)
      n[i] = 4
    else:
      v = "012-=".index(str(n[i]))
      n[i] = v - 1
  return n

def toSnafu(d):
  n = numberToBase(d, 5)
  n1 = n.copy()
  n.reverse()
  for i, v in enumerate(n):
    if v == 4:
      if i < len(n)-1:
        n = carry(n, i)
      else:
        n.append(1)
      n[i] = "-"
    if v == 3:
      if i < len(n)-1:
        n = carry(n, i)
      else:
        n.append(1)
      n[i] = "="
  n.reverse()
  conv = "".join([str(i) for i in n])
  return conv

def fromSnafu(n):
  n = list(n)
  n.reverse()
  for i, v in enumerate(n):
    print(i,v)
    if str(v) in "-=":
      n = borrow(n, i+1)
      if n[i] == "-":
        n[i] = 4
      else:
        n[i] = 3
  # n.reverse()
  conv = sum([(5**(i))*int(n) for i,n in enumerate(n)])
  return n, conv

def main(path):
  total = 0
  mismatch = []
  fromSnafu("1=")
  with open(path, "r") as fh:
    header = fh.readline()
    line = True
    while line:
      line = fh.readline().strip()
      if not line:
        break
      d = line.split()
      conv = toSnafu(int(d[1]))
      rev = fromSnafu(d[0])
      print (d, conv, rev)
      if (int(d[1]) != rev[-1]):
        print("MISMATCH")
        mismatch.append(str((d, conv, rev)))
      print("")

  #print(f'total: {total}')
  print("MISMATCH TOTAL")
  print("\n".join(mismatch))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)