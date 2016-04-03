#!/bin/python

import sys


time = raw_input().strip()
def change(x):
    if x < 10:
        return "0"+str(x)
    else:
        return str(x)
if time[8] == 'P' or time[8] == 'p':
    time = time[:-2]
    split_time = map(lambda x: int(x),time.split(':'))
    if split_time[0] != 12:
        split_time[0] = 12 + split_time[0]
    split_time = map(change,split_time)
    print ":".join(split_time)
else:
    time = time[:-2]
    split_time = map(lambda x: int(x),time.split(':'))
    if split_time[0] == 12:
        split_time[0] = 0
    split_time = map(change,split_time)
    print ":".join(split_time)