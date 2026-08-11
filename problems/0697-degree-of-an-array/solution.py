# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:00:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count = {}, {}
        best, degree = len(nums), 0
        for i, value in enumerate(nums):
            first.setdefault(value, i)
            count[value] = count.get(value, 0) + 1
            if count[value] > degree:
                degree = count[value]
                best = i - first[value] + 1
            elif count[value] == degree:
                best = min(best, i - first[value] + 1)
        return best
