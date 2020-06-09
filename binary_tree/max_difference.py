class ResultWrapper:
    def __init__(self):
        self.global_max = -1
        self.solution = None

    def max_diff_node(root, res):
        if not root:
            return 0
        left_total = max_diff_node(root.left, res)
        right_total = max_diff_node(root.right, res)
        if abs(left_total - right_total) > res.global_max:
            res.global_max = abs(left_total - right_total)
            res.solution = root
        return left_total + right_total + 1

    def max_diff(root):
        res = ResultWrapper()
        max_diff_node(root, res)
        return res.solution

#T: O(n)
#S: O(h)

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.right = TreeNode(6)

res = max_diff(root)
print(res)

