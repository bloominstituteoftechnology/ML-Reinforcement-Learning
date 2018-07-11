def reward(R, gamma):
	# return -1.0  # TODO

	# Method 1
	# return R / (1 - gamma)

	# Method 2
	return sum([(gamma**k) * R for k in range(10000)])

	# Method 3
	# k = 0
	# coef = gamma**k
	# total = 0
	# while coef > 0.000001:
	# 	total += coef * R
	# 	k += 1
	# 	coef = gamma**k
	#
	# return total
