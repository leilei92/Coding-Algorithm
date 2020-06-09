# get tree height
def get_height(root):
    if not root:
        return 0
    left = get_height(root.left)
    right = get_height(root.right)
    return 1 + max(left, right)

#T: O(n)
#S: O(h)

# get minimum height
def get_height(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = get_height(root.left) if root.left else float('inf')
    right = get_height(root.right) if root.right else float('inf')
    return min(left, right) + 1

#T: O(n)
#S: O(h)
