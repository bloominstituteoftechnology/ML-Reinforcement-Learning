def reward(R, gamma):
	expR = 0
	for k, reward in enumerate(R):
		expR += gamma**k*reward
	return expR
