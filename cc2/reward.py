def reward(R, gamma):
	expR = 0
	k = 0
	while coef > 0.000001:
		expR += gamma**k*reward
	return expR
