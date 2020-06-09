#input: int target, int[] coins, return: int[][]


class Solution(object):
  def combinations(self, target, coins):
    res, cur = [], []
    self.bt(0, target, coins, cur, res)
    return res


  def bt(self, index, target, coins, cur, res):
    if index == len(coins) - 1:
      if target % coins[index]== 0:
        cur.append(target // coins[index])
        res.append(cur[:])
        cur.pop()
      return
    for num in range(0, target //coins[index] + 1):
      cur.append(num)
      self.bt(index + 1, target - num * coins[index], coins, cur, res)
      cur.pop()