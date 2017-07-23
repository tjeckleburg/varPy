#! /home/hda/anaconda3/bin/python
'''Version using a dict memo'''

import sys
import time

def fibo(n,memo):
    if n not in memo:
        memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
    return memo[n]

def main():
    #n = int(sys.argv[1])
    n = 998
    t0 = time.time()
    memo = {0:0, 1:1}
    f=fibo(n,memo)
    t1 = time.time()
    dt = t1 - t0
    print(f, dt)


if __name__ == '__main__':
    main()

