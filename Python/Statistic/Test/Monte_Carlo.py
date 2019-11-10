# モンテカルロ法でlog2を値を数値計算

import numpy as np
from numpy.random import rand


def MonteCarlo(f_in, n=10000):
    """
    paramators
    ___________
    n: int (default 10000)
        シミュレートする回数

    f_in: function
        抽出したい母集団のcdfの逆関数
    ___________

    return
    ___________
　　　　Y_: int
        log2の値の一致推定量
    ___________
    """

    X = sampling(n)
    Y = f_in(X)
    Y_ = np.mean(Y)
    return Y_


def sampling(n=10000):
    return rand(n)


def f_in(x):
    return 1 / (1 + x)


if __name__ == '__main__':
    n = 10000
    Y_ = MonteCarlo(f_in, n)
    print("log2の推定値は{}です".format(Y_))
    print("誤差は{}です".format(np.abs(np.log(2) - Y_)))
