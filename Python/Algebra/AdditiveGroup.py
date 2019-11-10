# 加法群
# 加法ついて群をなす（可換）

from abc import abstractclassmethod, ABCMeta
from typing import TypeVar

AdditiveGroupType = TypeVar("AdditiveGroupType", bound="AdditiveGroup")


class AdditiveGroup(metaclass=ABCMeta):

    # 加法
    @abstractclassmethod
    def __add__(self: AdditiveGroup, x: AdditiveGroup) -> AdditiveGroup:
        pass

    @abstractclassmethod
    #　零元
    def zero(self: AdditiveGroup) -> AdditiveGroup:
        pass

    @abstractclassmethod
    # 逆元
    def __neg__(self: AdditiveGroup) -> AdditiveGroup:
        pass

    # 差
    def __sub__(self: AdditiveGroup, x: AdditiveGroup) -> AdditiveGroup:
        return self + (-x)

    @abstractclassmethod
    # イコール
    def __eq__(self, x):
        pass

    # 結合律
    def testAdditiveAssociation(self: AdditiveGroup, a: AdditiveGroup, b: AdditiveGroup) -> bool:
        return (self + a) + b == self + (a + b)

    # 零元
    def testZero(self: AdditiveGroup) -> bool:
        return self + self.zero() == self

    # 零元の存在
    def testNegative(self: AdditiveGroup) -> bool:
        return self + (-self) == self.zero()

    # 可換
    def testAbelian(self: AdditiveGroup, a: AdditiveGroup) -> bool:
        return self + a == a + self
