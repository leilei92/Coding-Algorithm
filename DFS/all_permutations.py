class Solution(object):
  def permutations(self, input):
    answers, permutation = [], []
    self.bt(answers, 0, len(input), input)
    return answers

  def bt(self, answers, permutation, N, input):
    if len(permutation) == N:
      answers.append(permutation[:])
      return
    for i in input:
      if i not in permutation:
        permutation.append(i)
        self.bt(answers, permutation, N, input)
        permutation.pop()
    return