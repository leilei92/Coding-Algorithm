# recursion
class Solution(object):
  def preorderTraversal(self, root):
    res = []
    self.helper(root, res)
    return res

  def helper(self, root, res):
    if not root:
      return 0
    res.append(root.val)
    self.helper(root.left, res)
    self.helper(root.right, res)

#T: O(n)
#S: O(h)

# non-recursion
class Solution(object):
  def preOrder(self, root):
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
      if count ==1:
        output.append(node.val)
        stack.append((node, count +1))
        if node.left:
          stack.append((node.left, 1))
      if count ==2:
        if node.right:
          stack.append((node.right, 1))
    return output

#T: O(n)
#S: O(h)