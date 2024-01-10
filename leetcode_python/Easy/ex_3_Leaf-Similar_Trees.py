# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_values(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            get_leaf_values(root.left, leaves)
            get_leaf_values(root.right, leaves)
        
        leaves1, leaves2 = [], []
        
        # Get leaf values for the first tree
        get_leaf_values(root1, leaves1)
        
        # Get leaf values for the second tree
        get_leaf_values(root2, leaves2)
        
        # Compare the leaf value sequences
        return leaves1 == leaves2
    
# Example usage:
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.left.right.left = None
root2.left.right.right = None
root2.right.left = None
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

solution = Solution()
result = solution.leafSimilar(root1, root2)
print(result)  # Output: True
