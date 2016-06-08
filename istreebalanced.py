"""
Given a binary tree, determine if it is height-balanced.
"""

def height(root):
        if not root:
            return 0
        else:
            return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
        if not root:
            return True
        elif abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return isBalanced(root.left) and isBalanced(root.right)
    
    