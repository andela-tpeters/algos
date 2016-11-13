def bin(n):
  if n > 255:
    print "Out of range"
    return None
  
  result = []
  if(n==0):
    result.append(n)
  else:
    while n != 0:
      result.append(str(n%2))
      n /= 2
  
  result.reverse()
  print int("".join(result))
