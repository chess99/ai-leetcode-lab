# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:19:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num in nums:
            if num % 2 == 0 and frequency[num] == 1:
                return num
        return -1
