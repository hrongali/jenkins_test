import unittest
import main

class Test_Main(unittest.TestCase):
	def test_add_nums(self):
		self.assertEqual(main.add_nums(1,2),3)
		self.assertEqual(main.sub_nums(3,1),2)


if __name__=="__main__":
	unittest.main()
