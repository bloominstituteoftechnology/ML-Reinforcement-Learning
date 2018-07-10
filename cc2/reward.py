# MY ATTEMPT
'''
import random
gamma = random.uniform(0, 1)
k = 0 

# def reward(R, gamma):
	step = k + 1 
	R = 
	gamma = sum(R,step)
	return -1.0  

# CLASS 

def reward(R, gamma):
	# R is reward for a round
	# gamma is discount factor
	return R / (1 - gamma) # Navjot's Solution
	sum([(gamma**k) * R for k in range(10000)]) # Marina's Solution
	# return -1.0  
'''

# AARON'S ATTEMPT
	
def reward(R, gamma):
	k = 0 
	coef = gamma ** k # coefficient
	total = 0
	while coef > 0.000001:
		total += coef * R
		k += 1
		coef = gamma ** k
	return total 


