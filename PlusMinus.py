import sys
from decimal import Decimal

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pInt = 0
nInt = 0
zeros = 0

for i in arr:
    if i > 0:
        pInt += 1
    elif i < 0:
        nInt += 1
    else:
        zeros += 1
        
print "%.6f" % (Decimal(pInt)/Decimal(n))
print "%.6f" % (Decimal(nInt)/n)
print "%.6f" % (Decimal(zeros)/n)