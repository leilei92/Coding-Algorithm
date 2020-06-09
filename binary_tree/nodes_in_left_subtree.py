def change_subtree(node):
    if node is None:
        return 0
    left_total = change_subtree(node.left)
    right_total = change_subtree(node.right)
    node.total_left = left_total
    return 1 + left_total + right_total

#T: O(n)
#S: O(h)