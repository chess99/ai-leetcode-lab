# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect_right
        nums.sort()
        for i in range(1, len(nums)): nums[i] += nums[i-1]
        return [bisect_right(nums, query) for query in queries]
