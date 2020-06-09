#Find the second large number in a binary search tree
#binary search tree with in order traverse (right first)
#get desc order
#add a counter

class Solution(object):
    def secondLargest(self, root):
        self.cnt = 0
        self.result = None
        self.traverse(root)
        return self.result if self.result != None

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.right)
        self.cnt += 1
        if self.cnt == 2:
            self.result = root.val
            return
        if self.cnt > 2: # complexity decreased to O(h)
            return
        self.traverse(root.right)