def reward(R, gamma):
	return sum([gamma**k*R for k in range(10000)])  # TODO
