import sys

print "enter number: "
n = int(raw_input().strip())

a = []
for a_i in xrange(n):
    print "next: "
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

first_sum = 0
second_sum = 0
for i in xrange(n):
    first_sum += a[i][i]
    second_sum += a[n-1][i]
    n -= 1

print abs(first_sum - second_sum)

