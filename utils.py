class Utils:
	def __str__(self):
		string_list = ['%s' % self.__class__]
		for attr in self.__dict__:
			string_list.append(' %s: %s' % (attr,self.__dict__[attr]))
		return '\n'.join(string_list)
