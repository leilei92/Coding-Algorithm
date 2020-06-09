# given n pairs of parenthese, write a function to generate
# all combinations of well-formed parentheses
# for example: n = 3



class Solution(object):
    def validParentheses(self, n):
        answers, sequence = [], []
        self.bt(answers, sequence, n, 0, 0)
        return answers

    def bt(self, answers, sequence, n, l, r):
        if l == r == n: # len(sequence) == 2*n
            answers.append(''.join(sequence))
            return
        if l < n:
            sequence.append('(')
            self.bt(answers, sequence, n, l + 1, r)
            sequence.pop()
        if l > r:
            sequence.append(')')
            self.bt(answers, sequence, n, 1, r + 1)
            sequence.pop()