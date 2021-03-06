# https://leetcode.com/problems/path-sum/description/


"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N * M)
Memory: O(N * M) in worst case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val - sum == 0:
            return True
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
