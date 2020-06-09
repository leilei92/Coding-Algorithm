# recursion
class Solution(object):
  def postOrder(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    res = []
    self.helper(root, res)
    return res

  def helper(self, root, res):
    if not root:
      return 0
    self.helper(root.left, res)
    self.helper(root.right, res)
    res.append(root.val)
#T: O(n)
#S: O(h)

# non-recursion
class Solution(object):
  def postOrder(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    output = []
    if not root:
      return output
    stack = [(root, 1)]
    while stack:
      node, count = stack.pop()
      if count == 1:
        stack.append((node, count + 1))
        if node.left:
          stack.append((node.left, 1))
      if count == 2:
        stack.append((node, count + 1))
        if node.right:
          stack.append((node.right, 1))
      if count == 3:
        output.append(node.val)
    return output

#T: O(n)
#S: O(h)