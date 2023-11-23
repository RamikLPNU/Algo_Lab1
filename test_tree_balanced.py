import unittest
from tree_balanced import *

class TestIsBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root1 = BinaryTree(1)
        root1.left = BinaryTree(2)
        root1.right = BinaryTree(3)
        root1.left.left = BinaryTree(4)
        root1.left.right = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root1))

    def test_unbalanced_tree(self):
        root2 = BinaryTree(1)
        root2.left = BinaryTree(2)
        root2.right = BinaryTree(3)
        root2.right.right = BinaryTree(4)
        root2.right.right.right = BinaryTree(5)
        self.assertFalse(is_tree_balanced(root2))

    def test_slightly_unbalanced_tree(self):
        root3 = BinaryTree(1)
        root3.left = BinaryTree(2)
        root3.right = BinaryTree(3)
        root3.right.left = BinaryTree(4)
        root3.left.left = BinaryTree(5)
        root3.left.left.left = BinaryTree(6)        
        self.assertFalse(is_tree_balanced(root3))
        
    def test_single_node_tree(self):
        root4 = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root4))

    def test_single_node_tree(self):
        root5 = BinaryTree(1)
        root5.left = BinaryTree(2)
        root5.left.left = BinaryTree(3)
        root5.left.right = BinaryTree(4)
        root5.left.left.left = BinaryTree(5)
        root5.left.left.right = BinaryTree(6)
        root5.left.left.left.left = BinaryTree(7)
        root5.right = BinaryTree(8)
        root5.right.left = BinaryTree(9)
        root5.right.right = BinaryTree(10)
        self.assertFalse(is_tree_balanced(root5))
    
    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))
            
if __name__ == '__main__':
    unittest.main()