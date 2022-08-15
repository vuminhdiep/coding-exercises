# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Complexity: time O(n), space O(n)
        if root is None:
            return 0
        return self.preprocess(root, False) #not reach the end left leaf node yet
        
    def preprocess(self, root, isLeft):
        leftSum = 0
        if root.left is None and root.right is None:
            if isLeft:
                return root.val
            else:
                return 0
        if root.left:
            leftSum += self.preprocess(root.left, True)
        if root.right:
            leftSum += self.preprocess(root.right, False)
        return leftSum
        