def reward(R, gamma, max_steps=1000):
    return sum(R*gamma**step for step in range(max_steps))