def reward(R, gamma):
	rew = 0
	for n in range(1000): rew += R * (gamma ** n)
	return rew

	