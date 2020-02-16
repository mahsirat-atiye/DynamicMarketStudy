import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

# parameters:
# n = 2048
# n = 10
# m = 256
# m = 2
# x = [0] * n
# x = [0, 0.1, 0.75, 0.75, 0.1, 0, -0.1, -0.75, -0.75, -0.1]

# -----------------------------------------
import xlrd

wb = xlrd.open_workbook("dedam5.xlsx")
sheet = wb.sheet_by_index(0)
# For row 0 and column 0
print(sheet.cell_value(0, 5))
n = 2048
y = sheet.cell_value(1, 5)
x = [y] * n

for i in range(2048):
    x[i] = sheet.cell_value(1 + i, 5)
t = [i for i in range(n)]
m = 256

def get_t_by_k(k):
    return m / 2 * k


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


for k in range(n // m):
    a = [I(0, 0)] * n
    for j in range(n):
        print("j: ", j, ", k: ", k, ", d: ", I(j, k))
        a[j] = I(j, k)
    b = [I(0, 0)] * n
    b[0] = a[0]
    b[1] = (a[0] + a[1]) / 2
    for k_ in range(2, n - 2, 1):
        b[k_] = (a[k_ - 2] + 2 * a[k_ - 1] + 3 * a[k_] + 2 * a[k_ + 1] + a[k_ + 2]) / 9
    b[n - 2] = (a[n - 3] + a[n - 2] + a[n - 1]) / 3
    b[n - 1] = (a[n - 2] + a[n - 1]) / 2
    fig, ax = plt.subplots()
    ax.plot(t, b)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Signal amplitude' + str(k))
    plt.show()
