#! /home/hda/anaconda3/bin/python
import sys
import time

def fibo(n,memo):
    if (n==0 or n==1):
        memo[n] = n
        return n
    else:
        if memo[n] != None: 
            return memo[n]
        else:
            memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
            return memo[n]

def main():
    n = int(sys.argv[1])
    t0 = time.time()
    memo = [None]*(n+1)
    f= fibo(n, memo)
    t1 = time.time()
    dt = t1 - t0
    print(f, dt)
    

if __name__ == '__main__':
    main()
