# 群
# モノイドに加えて、逆元の存在

from Algebra.Monoid import Monoid
from abc import abstractclassmethod, ABCMeta
from typing import TypeVar

GroupType = TypeVar('GroupType', bound='Group')


class Group(Monoid, metaclass=ABCMeta):
    # 逆元
    @abstractclassmethod
    def inverse(self: GroupType) -> GroupType:
        pass

    # 除算
    @abstractclassmethod
    def __truediv__(self: GroupType, x: GroupType) -> GroupType:
        return self * x.inverse()

    # 逆元
    def testInverse(self: GroupType) -> bool:
        return self * self.inverse() == self.identity()
