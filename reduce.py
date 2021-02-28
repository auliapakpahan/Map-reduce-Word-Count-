#!/usr/bin/env python

import sys
from collections import Counter

def run_reduce(f):
    cnt = Counter()
    for line in f:
        data = line.rstrip()
        cnt[data] += 1
    for word, count in cnt.items():
        print(word, ':',count)

if __name__ == '__main__':
    run_reduce(sys.stdin)