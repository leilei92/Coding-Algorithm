from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# follow up question
# print line by line separately
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            count = len(queue) #add a counter to remember current level's size
            current_level = []
            for _ in range(count): #should not use range(len(queue)) because len(queue) is always changing
                node = queue.popleft()
                current_level.append(node.left)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
#T: O(n)
