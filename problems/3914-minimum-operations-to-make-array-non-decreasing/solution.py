# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        dravonikel = nums
        return sum(max(0, left - right) for left, right in zip(dravonikel, dravonikel[1:]))
