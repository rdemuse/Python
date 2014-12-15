import time
import functools

def timeandcount(f):
	'''Decorator that counts how many times f has
	been called and for each call, how long it 
	takes to execute f'''
	dict = {}
	def wrapper(*args,**kwargs):
		wrapper.count += 1
		start = time.time()
		result = f(*args,**kwargs)
		end = time.time()
		dict[wrapper.count] = end - start
		return result
	wrapper.count = 0
	return wrapper

if __name__ == '__main__':

	@timeandcount	
	def countdown(n): 
		while n > 0: n -= 1

	for i in range(10): countdown(1000)

	@timeandcount
	def sum(n): 
		functools.reduce(lambda x, y: x+y, range(n))

	for i in range(10): sum(10000)

	print('countdown(1000)')
	print(countdown.__closure__[0].cell_contents)
	print('sum(1000)')
	print(sum.__closure__[0].cell_contents)
