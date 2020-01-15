# quadratic weighted kappa
# マルチクラス分類問題での評価指標

from sklearn.metrics import confusion_matrix, cohen_kappa_score


def quadratic_weighted_kappa(c_matrix):
    """
    qwkを計算

    parametors
    __________
    c_matrix: ndarray
        混同行列
    __________
    """

    numer = 0.0
    denom = 0.0

    for i in range(c_matrix.shape[0]):
      for j in range(c_matrix.shape[1]):
        




