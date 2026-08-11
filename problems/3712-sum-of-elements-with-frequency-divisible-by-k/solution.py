# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return sum(num * count for num, count in counts.items() if count % k == 0)
