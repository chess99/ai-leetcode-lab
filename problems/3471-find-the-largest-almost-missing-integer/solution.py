# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {}
        for start in range(len(nums) - k + 1):
            for num in set(nums[start:start + k]):
                counts[num] = counts.get(num, 0) + 1

        return max((num for num, count in counts.items() if count == 1), default=-1)
