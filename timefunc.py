import time
from functools import wraps

def timefunc(f):
	'''Decorator that reports the execution time of f.'''
	@wraps(f)
	def wrapper(*args,**kwargs):
		start = time.time()
		result = f(*args,**kwargs)
		end = time.time()
		print(f.__name__,end-start)
		return result
	return wrapper

@timefunc
def countdown(n):
	'''Counts down from n to 0'''
	while n>0: n-=1


@timefunc
def fibo(n):
	f0 = f1 = f2 = 1
	for i in range(n-1):
		f0 = f1 + f2
		f2, f1 = f1, f0
	return f0				
