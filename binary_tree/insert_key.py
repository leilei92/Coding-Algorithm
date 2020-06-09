class BST(object):
    def _insert(self, root, key, value):
        if not root:
            return _Node(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value
        return root
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)

# implement this iteratively

class BST(object):
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        if not self._root:
            self._root = _Node(key, value)
            return
        curr, prev, is_left = self._root, None, None
        while curr:
            prev = curr
            if key < curr.key:
                is_left = True
                curr = curr.left
            elif key > curr.key:
                is_left = False
                curr = curr.right
            else:
                curr.value = value
                break
        if not curr:
            node = _Node(key, value)
        if is_left:
            prev.left = node
        else:
            prev.right = node
