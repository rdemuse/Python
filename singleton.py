'''Enforce a single instance of every subclass of Singleton'''
class Singleton:
	_singleton = {}
	def __new__(cls,*args,**kwargs):
		if cls in Singleton._singleton: return Singleton._singleton[cls]
		else: obj = Singleton._singleton[cls] = object.__new__(cls)
		return obj
