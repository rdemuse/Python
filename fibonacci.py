# Fibonacci program using caching 

class Cache:
	def __init__(self,f):
		self._f = f
		self.cache = {}

	def __call__(self,n):
		try:
			return self.cache[n]
		except:
			self.cache[n] = self._f(n)
			return self.cache[n]

@Cache
def fibo(n):
	f0 = f2 = f1 = 1
	for i in range(n-1): 
		f0 = f1 + f2
		f2, f1 = f1, f0
	return f0
