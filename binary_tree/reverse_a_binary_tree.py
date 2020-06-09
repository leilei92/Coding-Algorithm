def upside_tree(root):
    if not root:
        return root
    if not root.left and not root.right:
        return root
    new_root = upside_tree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return new_root

#T: O(n)
#S: O(h)