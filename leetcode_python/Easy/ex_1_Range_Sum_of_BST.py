# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        # Base case: if the root is None, return 0
        if not root:
            return 0
        
        # Check if the current node value is not None and within the range [low, high]
        if root.val is not None and low <= root.val <= high:
            current_sum = root.val
        else:
            current_sum = 0
        
        # Recursively calculate the sum for left and right subtrees
        current_sum += self.rangeSumBST(root.left, low, high)
        current_sum += self.rangeSumBST(root.right, low, high)
        
        return current_sum

# Construct the binary search tree
tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(7)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(None)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(18)
tree.left.left.left = TreeNode(1)
tree.left.right.right = TreeNode(6)

solver = Solution()
print(solver.rangeSumBST(tree, low=6, high=10))
