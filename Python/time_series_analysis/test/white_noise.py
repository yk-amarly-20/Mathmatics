import sys
sys.path.append("../../../")
from Python.time_series_analysis import white_noise
import matplotlib.pyplot as plt

def test():
    dlen = 5
    mean = 0.0
    std = 1.0

    x = [0, 1, 2, 3, 4]
    y = white_noise(dlen, mean, std)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    test()
