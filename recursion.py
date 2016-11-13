def sum(n):
  if n < 10:
    return n
  else:
    rem = str(n)[0:-1]
    numb = int(str(n)[-1])
    return numb + sum(int(rem))


def root(n):
    return sum(sum(n))
