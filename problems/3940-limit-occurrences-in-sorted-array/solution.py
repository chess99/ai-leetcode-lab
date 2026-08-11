# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:23:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        result = []
        count = 0
        previous = None
        for num in nums:
            if num != previous:
                previous = num
                count = 0
            count += 1
            if count <= k:
                result.append(num)
        return result
