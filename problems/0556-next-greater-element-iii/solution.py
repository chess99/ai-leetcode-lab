# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        pivot = len(digits) - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return -1

        successor = len(digits) - 1
        while digits[successor] <= digits[pivot]:
            successor -= 1
        digits[pivot], digits[successor] = digits[successor], digits[pivot]
        digits[pivot + 1:] = reversed(digits[pivot + 1:])

        result = int("".join(digits))
        return result if result <= 2**31 - 1 else -1
