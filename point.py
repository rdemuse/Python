import math
from singleton import Singleton

class Point(Singleton):

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def _getRadius(self):
		return math.sqrt(self.x**2 + self.y**2)
	
	def _getAngle(self):
		return math.atan2(self.y,self.x) % 2*math.pi

	r = property(_getRadius)
	theta = property(_getAngle)
