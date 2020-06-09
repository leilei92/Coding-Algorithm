# given a sorted list of chars with duplicated chars, return all possible subset.
# solution set must not contain duplicate subsets
# for example: input = abb; output = 1, b, ab, bb, abb

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

        while current_position + 1 < len(input) and input[current_position] = input[current_position] + 1
        current_position += 1
        self.bt(input, current_position + 1,  answers, subset)
        return
