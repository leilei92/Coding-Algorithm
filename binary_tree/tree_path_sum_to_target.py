#Given a binary tree and a target sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given target.

class Solution(object):
    def exist(self, root, target):
        """
        input: TreeNode root, int target
        return: boolean
        """
        return self.sumPath(root, 0, target)

    def sumPath(self, root, partial, target):
        if root is None:
            return False
        partial += root.val
        if root.left is None and root.right is None:
            return partial == target
        return self.sumPath(root.left, partial, target) or self.sumPath(root.right, partial, target)

#T: O(n)
#S: O(h)

#path: from one node to itself or to any of its descendants
class Solution(object):
    def exist(self, root, target):
        hash = dict()
        self.ret = False
        self.helper(root, target, hash, 0)
        return self.ret
    def helper(selfself, root, target, hash, cur):
        if root is None:
            return
        cur = cur + root.val
        if cur == target:
            self.ret = True
        if (cur-target) in hash and hash [(cur - target)] > 0:
            self.ret = True
        if cur in hash:
            hash[cur] += 1
        else:
            hash[cur] = 1

        self.helper(root.left, target, hash, cur)
        self.helper(root.right, target, hash, cur)

        hash[cur] -= 1
        return

#path: from one leaf node to another

def helper