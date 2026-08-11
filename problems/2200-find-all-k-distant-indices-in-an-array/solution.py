# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:20:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i, value in enumerate(nums) if value == key]
        return [i for i in range(len(nums)) if any(abs(i-j) <= k for j in keys)]
