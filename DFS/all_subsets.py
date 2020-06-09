class Solution(object):
  def subsets(self, input):
    answers, subset = [], []
    self.bt(input, 0, answers, subset)
    return answers

  def bt(self, input, current_position, answers, subset):
    if current_position == len(input):
      answers.append(subset[:])
      return

    subset.append(input[current_position])
    self.bt(input, current_position + 1, answers, subset)
    subset.pop()

    self.bt(input, current_position + 1, answers, subset)
    return