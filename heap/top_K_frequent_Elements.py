# given a non-empty array of integers, return the k most frequent elements
#input: nums=[1, 1, 4, 1, 2, 2], k = 2
#output: [1, 2]
#(3, 1), (2, 2), (1, 4)
import heapq

def topKFrenquentPQ(nums, k):
    freq_hash = dict()
    for n in nums:
        if n in freq_hash:
            freq_hash[n] += 1
        else:
            freq_hash[n] = 1

    heap = []
    for n, f in freq_hash.otems():
        heapq.heappush(heap, (f, n))
        if len(heap) > k:
            heapq.headppop(heap)

    ret = []
    while len(heap) != 0:
        ret.append(heapq.heappop(heap)[1])
    ret.reverse()
    return ret

# T: O(n) + O(nlogK) + O(klogk) + o(k)