import sys
sys.setrecursionlimit(2 ** 30)


def f(x):
    x(x)


f(f)
