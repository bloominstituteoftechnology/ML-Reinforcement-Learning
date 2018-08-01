R = 0
total = 0
coef = gamma**k

def reward(R, gamma):
    while coef > 0.000001:
	    total += coef
	    R += 1
	    coef = gamma**R
	 return total

#def reward(R, gamma):
#return -1.0
#def reward(R, gamma):
#return R/(1-gamma)

#sum([gamma**k*R for k in range(10000)])
