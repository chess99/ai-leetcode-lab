# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums),2): result.extend([nums[i+1]]*nums[i])
        return result
