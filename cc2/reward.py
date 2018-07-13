def reward(R, gamma):
	rew = 0
	for n in range(1000): rew += R * (gamma ** n)
	return rew
<<<<<<< HEAD

	
=======
>>>>>>> b83e05310205e0f6b15f1ce1c4780d06873901b2
