# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:03:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def massage(self, nums: List[int]) -> int:
        skip = take = 0
        for duration in nums:
            skip, take = max(skip, take), skip + duration
        return max(skip, take)
