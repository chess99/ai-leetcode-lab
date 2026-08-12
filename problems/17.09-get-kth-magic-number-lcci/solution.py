# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        values = [1] * k
        index3 = index5 = index7 = 0
        for index in range(1, k):
            next_value = min(values[index3] * 3,
                             values[index5] * 5,
                             values[index7] * 7)
            values[index] = next_value
            while values[index3] * 3 <= next_value:
                index3 += 1
            while values[index5] * 5 <= next_value:
                index5 += 1
            while values[index7] * 7 <= next_value:
                index7 += 1
        return values[-1]
