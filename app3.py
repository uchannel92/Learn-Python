import unittest
from app import Dog

class NameTestCase(unittest.TestCase):
	"""Creating test for app.py """

	def test_wag_tail(self):
		'''' does the wag tail method work'''
		test = Dog('chiuwawa', 'Coco')
		self.assertEqual(test.wag_tail(), 'chiuwawa wags tail')

	def test_dog_bark(self):
		'''' Does the dog bark '''
		test = Dog()
		self.assertEqual(test.dog_bark(), 'woof!')
		
if __name__ == '__main__':
	unittest.main()


