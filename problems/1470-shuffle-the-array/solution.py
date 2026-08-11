# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:03:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for index in range(n):
            result.extend((nums[index], nums[index + n]))
        return result
