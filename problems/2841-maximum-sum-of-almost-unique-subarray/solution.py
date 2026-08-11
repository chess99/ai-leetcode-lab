# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        count=defaultdict(int); total=answer=distinct=0
        for i,x in enumerate(nums):
            if count[x]==0: distinct+=1
            count[x]+=1; total+=x
            if i>=k:
                old=nums[i-k]; count[old]-=1; total-=old
                if count[old]==0: distinct-=1
            if i>=k-1 and distinct>=m: answer=max(answer,total)
        return answer
