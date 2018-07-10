import sys
import mpmath
from sympy.mpmath import *

def reward(R, gamma):
	rBig = nsum(lambda k: gamma^k * R, [0, inf])
	return rBig # TODO
