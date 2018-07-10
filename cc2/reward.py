def reward(R, gamma):
	tot_rew = 0
	for i in range(1000):
		rew = (R)*(gamma**i)
		tot_rew += rew
	return tot_rew