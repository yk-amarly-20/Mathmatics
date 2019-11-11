# 棄却アルゴリズム
# 乱数生成アルゴリズムの一種
# 予測分布から直接乱数を生成するのは難しいので、乱数生成が容易な提案分布　（一様分布がいい）から生成する

# 例として予測分布をβ分布とする

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize as opt
from scipy.stats import beta, uniform


def optimize_beta(a, b):
    """
    β分布の最適化(最大値を求める)を実行

    paramaters
    ___________
    a: int 
        β分布のパラメータ1

    b: int
        β分布のパラメータ2
    ___________

    return
    ___________
    res: int
      　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　argmax(beta.pdf)

    M: int
        β分布の最大値
    ___________
    """

    f = beta(a=a, b=b).pdf
    res = opt.fmin(lambda x: -f(x), 0.1)  # 最小値問題に帰着する為に-をつける
    M = f(res)
    print("β分布はx={0}で最大値{1}をとります".format(res, M))

    return res, M


def sampling(n=1000):
    """
    一様分布の乱数を生成
    """

    f = beta(a=a, b=b).pdf
    _, M = optimize_beta(a=1.8, b=2.9)
    y = uniform.rvs(size=n)
    mq = M * uniform.rvs(size=n)
    accept = y[mq <= f(y)]

    return accept


def data_plot(a, b, n):
    """
    β分布、乱数生成結果をプロット
    """
    accept = sampling(n)
    plt.hist(accept, normed=True, bins=35,
             rwidth=0.8, label="rejection_sampling")
    x = np.linspace(beta.pdf(0.001, a, b), np.linspace(0.999, a, b), 100)
    plt.plot(x, beta.pdf(x, a, b), label="target")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    a = 1.8
    b = 2.9
    n = 30000

    data_plot(a, b, n)
