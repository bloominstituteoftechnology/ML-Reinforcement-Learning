def reward(R, gamma):
    return R/(1-gamma)

def reward2(R, gamma):
    total_reward = 0
    k = 0
    coeff = gamma**k
    while coeff > 0.000001:
        total_reward += R*coeff
        k += 1
        coeff = gamma**k
    return total_reward

def reward3(R, gamma):
    return sum([R*(gamma**k) for k in range(10000)])
