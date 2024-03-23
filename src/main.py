from libarea import *

def main():
  tri = Triangle(3, 4, 5)
  print(tri.getArea())
  print(tri.isRect)

  cir = Circle(5)
  print(cir.getArea())

if __name__ == "__main__":
  main()