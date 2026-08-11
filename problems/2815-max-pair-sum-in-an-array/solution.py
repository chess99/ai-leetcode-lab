# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:24:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = [-1] * 10
        result = -1

        for num in nums:
            digit = max(map(int, str(num)))
            if best[digit] != -1:
                result = max(result, best[digit] + num)
            best[digit] = max(best[digit], num)

        return result
