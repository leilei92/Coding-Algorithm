# given two intergers n and k, return all possible combinations of k numbers out of 1....n
#e.g. input: n = 4, k = 2


class Solution(object):
  def combine(self, n, k):
    results, comb = [], []
    self.bt(results, comb, 1, n, k)
    return results

  def bt(self, results, comb, i, n, k):
    if k ==0:
      results.append(comb[:])
      return
    for t in range(i, n+1):
      comb.append(t)
      self.bt(results, comb, t + 1, n, k-1)
      comb.pop()