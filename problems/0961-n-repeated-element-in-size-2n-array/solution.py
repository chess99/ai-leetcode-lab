# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for value in nums:
            if value in seen: return value
            seen.add(value)
