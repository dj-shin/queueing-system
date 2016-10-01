import random
import math


def rand(range=1.0):
    return random.uniform(0.0, range)

def expntl(x):
    return (-x * math.log(rand()))
