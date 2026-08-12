# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        a=[(x>y)-(x<y) for x,y in zip(nums[1:],nums)];p=pattern
        prefix=[0]*len(p)
        for i in range(1,len(p)):
            j=prefix[i-1]
            while j and p[i]!=p[j]:j=prefix[j-1]
            if p[i]==p[j]:j+=1
            prefix[i]=j
        j=0;ans=0
        for x in a:
            while j and x!=p[j]:j=prefix[j-1]
            if x==p[j]:j+=1
            if j==len(p):ans+=1;j=prefix[j-1]
        return ans
