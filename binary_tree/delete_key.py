class BST(object):
    def __init__(self):
        self._root = None
    def _min(self, root):
        if not root.left:
            return root
        return self._min(root.left)
    def _deleteMin(self, root):
        if not root.left:
            return root.right
        root.left = self._deleteMin(root.left)
        return root
    def _delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            t = root
            root = self._min(t.right)
            root.right = self._deleteMin(t.right)
            root.left = t.left
        return root
    def delete(self, key):
        self._root = self._delete(self._root, key)