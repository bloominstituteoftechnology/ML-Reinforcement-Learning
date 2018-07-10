from math import log, ceil

def reward(R, gamma, epsilon=.000001):
    max_steps = ceil(log(epsilon, gamma))
    return sum(R*gamma**step for step in range(max_steps))