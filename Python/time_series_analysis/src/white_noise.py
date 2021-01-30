import sys
sys.path.append("../../../")
from Python.error.ValueMustPlusException import ValueMustPlusException
from typing import List, ValuesView
import numpy as np

def white_noise(dlen: int, mean: float, std: float) -> np.ndarray:

    try:
        if dlen <= 0:
            raise ValueMustPlusException("dlen", dlen)
        if std <= 0:
            raise ValueMustPlusException("std", std)
        y = np.random.normal(mean, std, dlen)

        return y

    except Exception as e:
         print(e)
