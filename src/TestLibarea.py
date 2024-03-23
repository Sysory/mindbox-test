import unittest
from libarea import Triangle, Circle

class TestLibArea(unittest.TestCase):
  def setUp(self):
    pass

  def test_triangle_rect1(self):
    tri = Triangle(5, 4, 3)
    self.assertEqual(tri.isRect, True)
  def test_triangle_rect2(self):
    tri = Triangle(3.3, 5.5, 4.4)
    self.assertEqual(tri.isRect, True)
  def test_triangle_rect3(self):
    tri = Triangle(3.3, 5.51, 4.4)
    self.assertEqual(tri.isRect, False)

  def test_triangle_valid1(self):
    tri = Triangle(1, 2, 3)
    self.assertEqual(tri.isValid, False)
  def test_triangle_valid2(self):
    tri = Triangle(3, 4, 5)
    self.assertEqual(tri.isValid, True)
  def test_triangle_valid3(self):
    tri = Triangle(3, -4, 5)
    self.assertEqual(tri.isValid, False)
  def test_triangle_valid4(self):
    tri = Triangle(3.3, 4.4, "jaba")
    self.assertEqual(tri.isValid, False)
  def test_triangle_valid5(self):
    tri = Triangle(70.3, 70.3, 70.3)
    self.assertEqual(tri.isValid, True)

  def test_triangle_area1(self):
    tri = Triangle(3, 4, 5)
    self.assertAlmostEqual(tri.getArea(), 6.0)
  def test_triangle_area2(self):
    tri = Triangle(17.2, 20.1, 20.1)
    self.assertAlmostEqual(tri.getArea(), 156.238593183)
  def test_triangle_area3(self):
    tri = Triangle(17.2, -20.1, 20.1)
    self.assertAlmostEqual(tri.getArea(), 0)
  
  def test_circle_valid1(self):
    cir = Circle(5.5)
    self.assertEqual(cir.isValid, True)
  def test_circle_valid2(self):
    cir = Circle(-5.5)
    self.assertEqual(cir.isValid, False)
  def test_circle_valid3(self):
    cir = Circle(0)
    self.assertEqual(cir.isValid, False)
  def test_circle_valid4(self):
    cir = Circle("jaba")
    self.assertEqual(cir.isValid, False)

  def test_circle_area1(self):
    cir = Circle("jaba")
    self.assertAlmostEqual(cir.getArea(), 0)
  def test_circle_area2(self):
    cir = Circle(10.2)
    self.assertAlmostEqual(cir.getArea(), 326.851299679)

if __name__ == "__main__":
  unittest.main()