def reward(R, gamma):
    # return -1.0
    k = 0
    total = 0
    coef = gamma**k
    while coef > 0.000001:
        total += coef * R
        k += 1
        coef = gamma**k
    return total
