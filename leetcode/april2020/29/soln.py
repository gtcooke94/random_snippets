# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.maxPathSumHelper(root))
    
    def maxPathSumHelper(self, node):
        if node is None:
            return -math.inf, -math.inf, -math.inf
        left, maybe_max1_ret2, ret31 = self.maxPathSumHelper(node.left)
        right, maybe_max2_ret2, ret32 = self.maxPathSumHelper(node.right)
        ret1 = max(node.val + left, node.val + right, node.val)
        ret2 = max(maybe_max1_ret2, maybe_max2_ret2, node.val + left + right)
        ret3 = max(ret1, ret2, ret31, ret32, node.val)
        return ret1, ret2, ret3
        
