from math import pi
# from abc import ABC, abstractmethod

class Figure:
  isValid = False
# class Figure(ABC):
  # @abstractmethod
  def getSquare() -> float:
    return None

class Triangle(Figure):

  def __init__(self, a : float, b : float, c : float):
    try: 
      if (a > 0 and b > 0 and c > 0):
        self.sides = (a, b, c)
        self.isValid = True
      else:
        raise Exception
    except:
      self.sides = (a, b, c)
      # self.a, self.b, self.c = 0, 0, 0

  def getSquare(self):
    if (not self.isValid): return 0

    a, b, c = self.sides
    s = (a + b + c) / 2 #полу-периметр
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
  
class RectTriangle(Triangle):
  pass


class Circle(Figure):
  def __init__(self, radius : float):
    try:
      if (radius > 0):
        self.radius = radius
        self.isValid = True
      else:
        raise Exception
    except:
      self.radius = 0

  def getSquare(self):
    return pi * self.radius * self.radius

