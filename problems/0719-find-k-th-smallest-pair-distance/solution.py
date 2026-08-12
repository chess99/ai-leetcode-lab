# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort();left,right=0,nums[-1]-nums[0]
        while left<right:
            mid=(left+right)//2;count=i=0
            for j in range(len(nums)):
                while nums[j]-nums[i]>mid:i+=1
                count+=j-i
            if count>=k:right=mid
            else:left=mid+1
        return left
