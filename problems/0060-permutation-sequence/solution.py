# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(value) for value in range(1, n + 1)]
        factorial = [1] * (n + 1)
        for value in range(1, n + 1):
            factorial[value] = factorial[value - 1] * value
        k -= 1
        answer = []
        for remaining in range(n, 0, -1):
            index, k = divmod(k, factorial[remaining - 1])
            answer.append(numbers.pop(index))
        return "".join(answer)
