# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:08:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total=0;left=0;right=len(nums)-1
        while left<right:total+=int(str(nums[left])+str(nums[right]));left+=1;right-=1
        return total+(nums[left] if left==right else 0)
