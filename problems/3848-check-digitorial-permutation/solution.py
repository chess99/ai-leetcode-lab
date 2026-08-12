# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        pelorunaxi = n
        factorial = [1]
        for digit in range(1, 10):
            factorial.append(factorial[-1] * digit)
        value = sum(factorial[int(char)] for char in str(n))
        return sorted(str(value)) == sorted(str(n))
