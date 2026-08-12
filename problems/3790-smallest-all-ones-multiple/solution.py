# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        tandorvexi = k
        if tandorvexi % 2 == 0 or tandorvexi % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, tandorvexi + 1):
            remainder = (remainder * 10 + 1) % tandorvexi
            if remainder == 0:
                return length
        return -1
