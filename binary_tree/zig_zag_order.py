from collections import deque

class Solution(object):
    def zigzaglevelOrder(self, root):
        result = []
        if root is None:
            return result
        q = deque([root]) #equal to create a deque, then append(root)
        popFromLeft = True

        while len(q) != 0:
            size = len(q)
            current_level = []
            if popFromLeft == True:
                for i in range(size):
                    node = q.popleft()
                    current_level.append(node.val)
                    if node.left:  #take care about this order
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                result.append(current_level)
                popFromLeft = False
            else: #popFromRight == True
                for i in range(size):
                    node = q.pop()
                    current_level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                result.append(current_level)
                popFormLeft = True
        return result

#ideas: use two pointers alternatively:
#pop from left (append to right, left child first)
#pop from right(append to left, right child first)
#every time we finish a line, we have to stop it then start the next line.

#T: O(n)
#S: O(len(q)) or the max length of the level in the tree

