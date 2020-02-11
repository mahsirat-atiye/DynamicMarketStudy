import math
import cmath

# parameters:

# n=2048
# m=256
# t=1…n
# {X_t:  t=1…n}
# ω_j=j/n
# t_k=128k;  k=0…14
# Daeniel Kernel Weights:  1/9 {1,2,3,2,1}
n = 2048
m = 256
x = [0] * 2048


def get_t_by_k(k):
    return 128 * k


def h(t):
    return 0.5 * (1 + (math.cos(math.pi * (2 * t - n - 1))) / n)


def sai(j, k, t):
    if t < get_t_by_k(k) or t > get_t_by_k(k) + m:
        return 0
    return math.sqrt(n / m) * h(t) * complex(math.cos(-2 * math.pi * t * j / m), math.sin(-2 * math.pi * t * j / m))


def d(j, k):
    sum = 0
    for t in range(n):
        sum += x[t] * sai(j, k, t)
    return sum / math.sqrt(n)


def I(j, k):
    r, phi = cmath.polar(d(j, k))
    return r ** 2
def f_hat_j(j):
    sum = 0
    for k in range(-m, m, 1):
        sum += Wm(k) * I()
