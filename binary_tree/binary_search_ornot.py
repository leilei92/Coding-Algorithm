class Solution(object):
  def isBST(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    min_val = float('-inf')
    max_val = float('inf')
    return self.helper(root, min_val, max_val)

  def helper(self, root, min_val, max_val):
    if root is None:
      return True
    if root.val <= min_val or root.val >= max_val:
      return False
    return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

#T: O(n)
#S: O(h)

