import heapq

def kSmallest(array, k):
    if not array:
        return array
    newArray = [-elem for elem in array[:]]
    res = []
    heapq.heapify(newArray)
    for i in range(min(k, len(newArray))):
        res.append(heapq.heappop(newArray))
    return [-elem for elem in res]

