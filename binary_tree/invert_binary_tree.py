class Solution(onject):
    def invertTree(self, root):
        if root is None:
            return root

        tmp_right = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp_right)
        return root

# create a temporary right root.

#T: O(n)
#S: O(logn)