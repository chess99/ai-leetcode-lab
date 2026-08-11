# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits, count, start = 1, 9, 1
        while n > digits * count: n -= digits * count; digits += 1; count *= 10; start *= 10
        number = start + (n - 1) // digits
        return int(str(number)[(n - 1) % digits])
