#!/usr/bin/env python

import sys

def run_map(f):
    for line in f:
        data = line.rstrip().split()
    for word in data:
        print(word)

if __name__ == '__main__':
    run_map(sys.stdin)