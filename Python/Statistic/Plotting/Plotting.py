# グラフ関係


def autocorrelation(data, h):
    """
    系列相関を計算
    
    Parameters
    --------------
    data : ndarray
        時系列データ
    h : int
        時点差
    
    Returns
    ---------
    r : double
        系列相関
    """

    length = len(data)
    data_front = data[:length - h]
    data_back = data[h:]  # 前半データと後半データ
    mean_front = np.mean(data_front)
    mean_back = np.mean(data_back)
    cov = (np.sum((data_front - mean_front) *
                  (data_back - mean_back))) / length  # 前半と後半の共分散

    std_front = np.std(data_front)
    std_back = np.std(data_back)  # 前半と後半の分散

    r = cov / (std_front * std_back)  # 系列相関

    return r