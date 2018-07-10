def reward(R, gamma):

	for i in range(20):

		discount = gamma ** (i+2)
		print(R)

		R += R*discount

	return R
