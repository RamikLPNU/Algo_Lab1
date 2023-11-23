class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def is_tree_balanced(root) -> bool:
    def tree(root):
        if not root:
            return [True, 0]

        left, right = tree(root.left), tree(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return tree(root)[0]

