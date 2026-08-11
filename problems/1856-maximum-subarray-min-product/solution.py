# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix=[0]
        for value in nums:prefix.append(prefix[-1]+value)
        stack=[];answer=0
        for i,value in enumerate(nums+[0]):
            while stack and nums[stack[-1]]>=value:
                index=stack.pop();left=stack[-1]+1 if stack else 0
                answer=max(answer,nums[index]*(prefix[i]-prefix[left]))
            stack.append(i)
        return answer%(10**9+7)
