from math import log, ceil

def reward(R, gamma, epsilon=.000001):
    return sum(R*gamma**step for step in range(ceil(log(epsilon, gamma))))