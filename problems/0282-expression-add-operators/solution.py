# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answer = []

        def search(index, expression, total, last):
            if index == len(num):
                if total == target:
                    answer.append(expression)
                return
            value = 0
            for end in range(index, len(num)):
                if end > index and num[index] == '0':
                    break
                value = value * 10 + ord(num[end]) - ord('0')
                piece = num[index:end + 1]
                if index == 0:
                    search(end + 1, piece, value, value)
                else:
                    search(end + 1, expression + '+' + piece,
                           total + value, value)
                    search(end + 1, expression + '-' + piece,
                           total - value, -value)
                    product = last * value
                    search(end + 1, expression + '*' + piece,
                           total - last + product, product)

        search(0, '', 0, 0)
        return answer
