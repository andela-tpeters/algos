def prime_number(number):
  sq_rt = int(number ** 0.5)

  if number == 1: return False;

  if number == 2 or number == 3: return True;

  if number % sq_rt == 0: return False;

  for i in range(2,sq_rt):
    if number % i == 0:
      return False
  else:
    return True


print "2: ",prime_number(2)
print "3: ",prime_number(3)
print "4: ",prime_number(4)
print "13: ",prime_number(13)
print "15: ",prime_number(15)
print "78: ",prime_number(78)