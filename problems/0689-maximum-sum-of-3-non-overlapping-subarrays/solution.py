# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums=[sum(nums[i:i+k])for i in range(len(nums)-k+1)];left=[0]*len(sums);best=0
        for i in range(len(sums)):
            if sums[i]>sums[best]:best=i
            left[i]=best
        right=[0]*len(sums);best=len(sums)-1
        for i in range(len(sums)-1,-1,-1):
            if sums[i]>=sums[best]:best=i
            right[i]=best
        answer=[];score=-1
        for mid in range(k,len(sums)-k):
            candidate=[left[mid-k],mid,right[mid+k]];value=sum(sums[i]for i in candidate)
            if value>score:score=value;answer=candidate
        return answer
