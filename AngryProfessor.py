#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    accepted = 0
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    
    for i in a:
        if i <= 0:
            accepted += 1
    
    if accepted < k:
        print "YES"
    elif accepted >= k:
        print "NO"