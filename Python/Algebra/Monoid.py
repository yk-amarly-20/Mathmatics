# モノイド
# 二項演算＊で閉じていて、結合法則、単位元の存在が言える

from typing import TypeVar
from abc import ABCMeta, abstractmethod

MonoidType = TypeVar('MonoidType', bound="Monoid")


class Monoid(metaclass=ABCMeta):
    # 乗算定義
    @abstractmethod
    def __mul__(self: MonoidType, x: MonoidType) -> MonoidType:
        pass

    # 単位元定義
    @abstractmethod
    def identity(self: MonoidType) -> MonoidType:
        pass

    # イコール定義
    @abstractmethod
    def __eq__(self: MonoidType, x: MonoidType) -> MonoidType:
        pass

    # 結合律
    @abstractmethod
    def testAssociativity(self: MonoidType, a: MonoidType, b: MonoidType) -> bool:
        return (self * a) * b == self * (a * b)

    # 単位元
    def testIdentity(self: MonoidType) -> bool:
        return self * self.identity() == self
