import numpy as np
import matplotlib.pyplot as plt

# ４次のルンゲクッタ法


def f(x, t):
    return - x ** 3 + np.sin(t)


a = 0.0
b = 10.0
N = 100
h = (b - a) / N

tpoints = np.arange(a, b, h)
xpoints = []
x = 0.0


def runge_kutta():

    # ルンゲクッタ法でdx/dt = f(t, x)を解く

    a = 0.0
    b = 10.0
    N = 100
    h = (b - a) / N

    tpoints = np.arange(a, b, h)
    xpoints = []
    x = 0.0

    for t in tpoints:
        xpoints.append(x)
        k1 = h * f(x, h)
        k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(x + k3, t + h)
        x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    plt.plot(tpoints, xpoints)
    plt.xlabel("$t$")
    plt.ylabel("$x$")
    plt.show()


if __name__ == "__main__":
    runge_kutta()
