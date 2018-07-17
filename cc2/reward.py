def reward(R, gamma):

	R_life = 0

	for k in range(20000):

		discount = gamma ** (k)
		R_life += R*discount

	return R_life
