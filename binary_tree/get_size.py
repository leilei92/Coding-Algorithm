def getSize(root):
    if not root:
        return 0
    left = getSize(root.left)
    right = getSize(root.right)
    return 1 + left + right