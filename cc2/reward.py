def reward(R, gamma):
	for k, reward in enumerate(R):
		expR += gamma**k*reward
	return expR
