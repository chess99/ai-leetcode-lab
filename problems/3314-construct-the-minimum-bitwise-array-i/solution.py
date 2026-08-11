# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
                continue

            bit = 1
            while num & bit:
                bit <<= 1
            result.append(num - (bit >> 1))

        return result
