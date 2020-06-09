class _None(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def _query(self, root, key):
        if not root:
            return None
        if key < root.value:
            return self._query(root.left, key)
        elif key > root.value:
            return self._query(root.right, key)
        else:
            return root.value

    def query(self, key):
        return self._query(self._root, key)

# implement this iteratively

class BST(object):
    def __init__(self):
        self._root = None

    def query(self, key):
        curr = self._root
        while curr:
            if key< curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.value
        return None