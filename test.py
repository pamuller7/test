from ft import mul, swap, ret_ascii, div
import unittest

class Testing_ft(unittest.TestCase):
	def test_mul(self):
		self.assertEqual(mul(3, 2), 6)
		self.assertEqual(mul(0, 651), 0)
		self.assertEqual(mul(3, -2), -6)

	def test_swap(self):
		self.assertEqual(swap(5, 9), (9, 5))
		self.assertEqual(swap('a', 'b'), ('b','a'))
	
	def test_ret_ascii(self):
		self.assertEqual(ret_ascii('a'), 97)
		self.assertEqual(ret_ascii('0'), 48)

class Testing_ft2(unittest.TestCase):
	def test_mul(self):
		self.assertEqual(mul(8, 1), 8)
		self.assertEqual(mul(0, 1), 0)
		self.assertEqual(mul(1, -6), -6)

	def test_swap(self):
		self.assertEqual(swap(5, 9), (9, 5))
		self.assertEqual(swap('a', 'b'), ('b','a'))
	
	def test_ret_ascii(self):
		self.assertEqual(ret_ascii('a'), 97)
		self.assertEqual(ret_ascii('0'), 48)

	def test_div(self):
		self.assertEqual(div(4,2), 2)
		self.assertEqual(div(4, 0), 0)

# if __name__ == '__main__':
# 	unittest.main()