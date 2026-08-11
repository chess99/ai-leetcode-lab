# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result=[]; value=0
        for bit in nums:
            value=(value*2+bit)%5; result.append(value==0)
        return result
