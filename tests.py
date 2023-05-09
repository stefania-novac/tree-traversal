import unittest
from tree import Tree

class TestTree(unittest.TestCase):
	def setUp(self):
		self.tree = Tree()

		self.tree.add(45)
		self.tree.add(17)
		self.tree.add(9)
		self.tree.add(3)
		self.tree.add(67)
		self.tree.add(16)

	def test_find_not_exists(self):
		result = self.tree.find(11)

		assert result is None

	def test_find_root(self):
		result = self.tree.find(45)

		assert result is not None
		assert result.data == 45

	def test_find_node(self):
		result = self.tree.find(3)

		assert result is not None
		assert result.data == 3

if __name__ == '__main__':
	unittest.main()
