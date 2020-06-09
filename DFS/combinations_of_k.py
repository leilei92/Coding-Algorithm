# given a list of size n (with no duplicate), print all possible combinations of k elements

class Solution(object):
    def subsets(self, input):
        answers, subset = [], []
        self.bt(input, 0, answers, subset, k)
        return answers

    def bt(self, input, current_position, answers, subset, k):
        if len(subset) == k:
            return
        if current_position == len(input):
            return

        subset.append(input[current_position])
        self.bt(input, current_position + 1, answers, subset, k)
        subset.pop()
        self.bt(input, current_position + 1, answers, subset, k)
        return

