from math import pi
# from abc import ABC, abstractmethod

class Figure:
  isValid = False
# class Figure(ABC):
  # @abstractmethod
  def getArea() -> float:
    pass
  
class Triangle(Figure):
  isRect = False

  def __init__(self, a : float, b : float, c : float):
    try:
      sides = (a, b, c)
      sides = sorted(sides)
      
      if (a > 0 and b > 0 and c > 0 and sides[2] < sum(sides[:2])):
        self.sides = sides
        self.isValid = True
      else:
        raise Exception
    except:
      self.sides = (0, 0, 0)
    else:
      if (self.sides[2]**2 == self.sides[0]**2 + self.sides[1]**2):
        self.isRect = True

  def getArea(self):
    if (not self.isValid): return 0

    a, b, c = self.sides
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
  

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

  def getArea(self):
    return pi * self.radius * self.radius

