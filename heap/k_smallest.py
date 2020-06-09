import heapq

# min_heap
import heapq


# Using min heap
def kSmallest(array, k):
    if not array:
        return array
    res = []
    heapq.heapify(array)
    for i in range(min(k, len(array))):
        res.append(heapq.heappop(array))
    return res


# Time: O(n) heapify all elements + O(klogN) pop k times
# Time: O(n+klogN)
# Space: O(n)

# max_heap
def kSmallest(array, k):
    if not array:
        return array
    res = [-i for i in array[0:k]]
    heapq.heapify(res)
    for i in range(k, len(array)):
        if array[i] < -res[0]:
            heapq.heappush(res, -array[i])
            heapq.heappop(res)

    return sorted([-i for i in res])
