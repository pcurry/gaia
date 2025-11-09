import random

# define dice rolling functions
def d100() -> int:
  return random.randint(1, 100)


def d6() -> int:
  return random.randint(1, 6)


def threeD6() -> int:
  return d6() + d6() + d6()


def twoD6() -> int:
  return d6() + d6()


def percentile_roll() -> float:
  return d100() / 100.0


_3d6 = threeD6
_2d6 = twoD6