import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
  def test_suma(self):
    self.assertEqual(calculadora.suma(1, 4), 5)

  def test_resta(self):
    self.assertEqual(calculadora.suma(1,4), 5)

  def test_multiplicacion(self):
    self.assertEqual(calculadora.multiplicacion(3,5),15)

  def test_division(self):
    self.assertEqual(calculadora.division(10,2),5)
  








if __name__== "__main__":
  unittest.main()