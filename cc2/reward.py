def reward(R, gamma):
	return -1.0  # TODO
	steps = int(input('How many steps predicted: '))
	return sum([gamma**k*R for k in range(steps)]) 
