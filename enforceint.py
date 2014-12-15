import functools

'''Class version of int enforcing decorator'''
class enforce_int_class:
	def __init__(self,f):
		self._f = f

	def __call__(self,*args):
		for n in args:
			if not isinstance(n,int):
				raise TypeError('All arguments must be integers.')
		return self._f(*args)

@enforce_int_class
def sumc(*args):
	return functools.reduce(lambda x, y: x+y, args)

print(str(sumc(1,2,3,4,5,6,7,8,9)))
#print(str(sumc(1.0,2.0,4,5,3,6,7,8,9)))


def enforce_int_func(f):
	def wrapper(*args):
		for n in args:
			if not isinstance(n,int):
				raise TypeError('All arguments must be integers.')
		return f(*args)
	return wrapper

@enforce_int_func
def sumf(*args):
	return functools.reduce(lambda x, y: x+y, args)

print(str(sumf(1,2,3,4,5,6,7,8,9)))
#print(str(sumf(1.0,2.0,3,4,5,6,7,8,9)))
