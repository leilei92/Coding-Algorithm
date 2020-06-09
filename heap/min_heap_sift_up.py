def sift_up(array, index):
    parent_index = (index - 1)//2
    if parent_index < 0 or array[index] > array[parent_index]: #parent_index < 0: index is root
        return                #array[index] > array[parent_index]: the number is already larger, do not need to sift up
    array[index], array[parent_index] = array[parent_index], array[index]
    sift_up(array, parent_index)

class Heap(object):
    def __init__(self):
        self.array = []

    def sift_up(self, array, index):
        parent_idx = (index - 1) //2
        if parent_index < 0 or array[index] > array[parent_index]:
            return
        array[index], array[parent_index] = array[parent_index], array[index]
        self.sift_up(array, parent_index)

    def push(self, val):
        self.array.append(val)
        self.sift_up(self.array, len(self.array)-1)


#Time: O(h) = O(logn)
#Space: O(h) = O(logn)