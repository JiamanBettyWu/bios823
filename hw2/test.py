import unittest
import sympy as sym

from find_first_prime import *


class TestGenExpansion(unittest.TestCase):
    def test_numbers(self):
        """
        Test for gen_expansion function.
        """
       
        result = gen_expansion(sym.pi, 2)
        self.assertEqual(result, '14')
        result = gen_expansion(sym.exp(1), 2)
        self.assertEqual(result, '72')
        
    def test_input_value(self):
        self.assertRaises(AttributeError, gen_expansion, int, 9)
        self.assertRaises(AttributeError, gen_expansion, 3.1, 9)
        self.assertRaises(AttributeError, gen_expansion, str, 9)
        self.assertRaises(ValueError, gen_expansion, sym.exp(1), -1)
        self.assertRaises(ValueError, gen_expansion, sym.exp(1), 1.5)

class TestIsPrime(unittest.TestCase):
    """ Test for the is_prime function。
    """
    def test_special_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(1223))
        self.assertFalse(is_prime(1224))
    
    def test_input_value(self):
        self.assertRaises(TypeError, is_prime, 3.1)
        self.assertRaises(ValueError, is_prime, -3)
        self.assertRaises(TypeError, is_prime, str)
    
class Test_sliding_window(unittest.TestCase):
    """ test for the sliding window function.
    """
    def test_input_value(self):
        self.assertRaises(AttributeError, sliding_window, "130300202", 1.2)
        self.assertRaises(AttributeError, sliding_window, 1, 1)
        self.assertRaises(AttributeError, sliding_window, str, -1)
        self.assertRaises(ValueError, sliding_window, '1111', 4)
        self.assertRaises(ValueError, sliding_window, '2222', 4)
        self.assertRaises(ValueError, sliding_window, 'sdsdsdddd', 4)
        self.assertRaises(AttributeError, sliding_window, '1222', str)
    
    def test_window(self):
        self.assertEqual(sliding_window('12941', 4), [1294, 2941])
        self.assertEqual(sliding_window('10941', 4), [1094])
    
    
class Test_main(unittest.TestCase):
    def test_1st_prime_e(self):
        """ Unit test for the final test given answers given that the first 10-digit prime in the expansion e is 7427466391.
        """
        self.assertEqual(main(sym.exp(1), 200, 10), 7427466391)
        

if __name__ == '__main__':
    unittest.main()