#! /home/hda/anaconda3/bin/python
import sys
import time

def fibo(n):
	if (n==0 or n==1) :
		return n
	else:
		return fibo(n-1) + fibo(n-2)

def main():
    n = int(sys.argv[1])
    t0 = time.time()
    f= fibo(n)
    t1 = time.time()
    dt = t1 - t0
    print(f, dt)
    

if __name__ == '__main__':
	main()
