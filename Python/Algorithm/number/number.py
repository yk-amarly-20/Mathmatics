# 整数系の問題


def gcd(a, b):
    """
  最大公約数

  parameters
  ___________
  a: int
  b: int

  returns
  ___________
  gcd: int
      最大公約数
  """

    if b == 0:
        return a
    return gcd(b, a % b)
