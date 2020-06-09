class Solution(object):
    def maxPathSumLeafToRoot(self, root):
        if root is None:
            return -float('inf')
        self.retValue = -float('inf')
        self.helper(root, 0)
        return self.retValue
    def helper(self, node, curSum):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.retValue = max(self.retValue, curSum + node.val)
            return
        self.helper(node.left, curSum + node.val)
        self.helper(node.right, curSum + node.val)