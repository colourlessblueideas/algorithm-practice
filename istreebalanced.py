"""
Given a binary tree, determine if it is height-balanced.
"""

def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

def isBalanced(self, root):
        if not root:
            return True
        elif abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    