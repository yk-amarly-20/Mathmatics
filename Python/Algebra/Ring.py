# 環
# 積についてモノイド
# 加法についてアーベル群

from Algebra.Monoid import Monoid
from Algebra.AdditiveGroup import AdditiveGroup
from typing import TypeVar

RingType = TypeVar('RingType', bound='Ring')


class Ring(Monoid, AdditiveGroup):
    # 分配法則
    def testDistributive(self: RingType, a: RingType, b: RingType) -> bool:
        return self * (a + b) == self * a + self * b
