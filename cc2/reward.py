def reward(R, gamma):
	return sum([gamma**k*R for k in range(1000)])  # TODO
