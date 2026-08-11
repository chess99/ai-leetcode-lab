# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:49:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        return max((counts[x] + counts[x + 1] for x in counts if x + 1 in counts), default=0)
