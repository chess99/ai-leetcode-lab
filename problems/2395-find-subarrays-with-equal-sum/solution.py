# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:59:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen=set()
        for index in range(len(nums)-1):
            total=nums[index]+nums[index+1]
            if total in seen:return True
            seen.add(total)
        return False
