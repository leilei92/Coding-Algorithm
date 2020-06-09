def level(root):
    q = [root]
    next = []
    line = []
    while q:
        head = q.pop()
        if head.left:
            next.append(head.left)
        if head.right:
            next.append(head.right)
        line.append(head.val)
        if not q:
            print(line)
            if next:
                q = next
                next = []
                line = []

#T: O(n)
#S: O(len(q))