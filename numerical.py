# numerical algorithms

# newton method

def newton(f, fprim, x0, e, maxIter):
	initMax = maxIter
	while maxIter > 0:
		x = x0 - f(x0) / fprim(x0)
		if abs(x - x0) < e:
			return x
		maxIter -= 1
		x0 = x
	
	print("Fail after %s iterations" % initMax)
