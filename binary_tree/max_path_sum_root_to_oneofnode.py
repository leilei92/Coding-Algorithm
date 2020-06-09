# on the path from root to one of the leaf nodes

self.global_max = -float('inf')
def helper(root):
    if root is None:
        return 0
    left_largest_sum = self.helper(root.left)
    right_largest_sum = self.helper(root.right)
    max_start_here = max(0, left_largest_sum, right_largest_sum) + root.value
    self.global_max = max(self.result, max_start_here)
    return max_start_here

def maxPathSumBinaryTree(self, root):
    self.result = -float('inf')
    self.helper(root)
    return self.global_max

#T: O(N)