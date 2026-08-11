# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:38:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for value in nums:
            if value == 0: return 0
            if value < 0: sign = -sign
        return sign
