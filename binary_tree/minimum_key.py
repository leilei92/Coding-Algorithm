class TreeNone(object):
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def FindMinimum(root):
        if not root:
            return None
        return FindMinimum(root.left) or root

# find first larger than target

    def FindFirstLargerThanTarget(root, target):
        if not root:
            return None
        if root.key == target:
            root FindMinimum(root.right)
        elif root.key < target:
            return FindFirstLargerThanTarget(root.right, target)
        else:
            return FindFirstLargerThanTarget(root.left, target) or root

# find last smaller than target

    def FindMaximum(root):
        if not root:
            return None
        return FindMaximum(root.right) or root

    def FindLastSmallerThanTarget(root, target):
        if not root:
            return None
        if root.key == target:
            return FindMaximum(root.left)
        elif root.key > target:
            return FindLastSmallerThanTarget(root.left, target)
        else:
            return FindLastSmallerThanTarget(root.right, target)
