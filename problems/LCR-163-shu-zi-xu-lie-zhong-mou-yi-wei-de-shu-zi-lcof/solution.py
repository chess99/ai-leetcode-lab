# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKthNumber(self, k: int) -> int:
        digits, start, count = 1, 1, 9
        while k > digits * count:
            k -= digits * count
            digits += 1
            start *= 10
            count *= 10
        number = start + (k - 1) // digits
        return int(str(number)[(k - 1) % digits])
