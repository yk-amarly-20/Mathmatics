# 整数環
from Algebra.Ring import Ring


class Integer(Ring):
    def __init__(self: "Integer", v: int) -> None:
        self.v = v

    def __repr__(self: "Integer") -> str:
        return str(self.v)

    def __mul__(self: "Integer", x: Integer) -> "Integer":
        return Integer(self.v * x.v)

    def __neg__(self: "Integer") -> "Integer":
        return Integer(-self.v)

    def __eq__(self, x):
        if not isinstance(x, Integer):
            return NotImplemented
        return self.v == x.v

    def identity(self: "Integer") -> "Integer":
        return Integer(1)

    def zero(self: "Integer") -> "Integer":
        return Integer(0)
