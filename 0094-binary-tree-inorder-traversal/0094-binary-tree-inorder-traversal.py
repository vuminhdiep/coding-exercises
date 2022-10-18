# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #inorderTraversal: use recursion
        #go left, node, right
        #O(H) space, O(n) time
        res = []
        self.helper(root, res)
        return res
      
    def helper(self, root, output):
        if root is None:
            return root
        else:
            self.helper(root.left, output)
            output.append(root.val)
            self.helper(root.right, output)
        
        