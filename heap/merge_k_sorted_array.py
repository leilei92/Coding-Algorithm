import heapq

class Solution(object):
    def merge(self, arrayOfArrays):
        heap = []
        for i in range(len(arrayOfArrays)):
            if len(arrayOfArrays[i]):
                heap.append((arrayOfArrays[i][0], i, 0))
        heapq.heapify(heap)
        result = []
        while heap:
            val, index_array, index_element = heapq.heappop(heap)
            result.append(val)
            if index_element + 1 < len(arrayOfArrays[index_array]):
                heapq.heappush(heap, (arrayOfArrays[index_array][index_element + 1], index_array, index_element + 1))
        return result

