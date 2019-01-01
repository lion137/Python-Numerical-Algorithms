# tests

import math
from numerical import *

def tests():
	print("test Newton Method")
	
	def f(x):
		return 2 * (x ** 2) - 1
	
	def fprim(x):
		return 4 * x
	
	assert  0.706 <= newton(f, fprim, 1, 0.001, 5) <= 0.708
	assert  -0.708 <= newton(f, fprim, -1, 0.001, 5) <= -0.706


tests()
	
