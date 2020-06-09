class Heap(object):
    def __init__(self):
        self.array = []

    def sift_down(self, array, index):
        left = index*2 +1
        right = index*2 +2
        small = index
        if left < len(array) and array[small] > array[left]:
            small = left
        if right < len(array) and array[small] > array[right]:
            small = right
        if small != index:
            array[small], array[index] = array[index], array[small]
            self.sift_down(array, small)
    def pop(self):
        res = self.array[0]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()
        self.sift_down(self.array, 0)
        return res