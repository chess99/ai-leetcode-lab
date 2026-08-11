# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:09:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(value * (((i + 1) * (len(arr) - i) + 1) // 2) for i, value in enumerate(arr))
