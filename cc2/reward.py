def reward(R, gamma):
  k = 0
  coef = gamma**k
  total = 0
  while coef >0.00001:
    total += coef *R
    k += 1
    coef = gamma**k
  return total
