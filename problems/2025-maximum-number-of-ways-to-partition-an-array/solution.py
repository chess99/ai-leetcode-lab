# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        from collections import Counter
        total=sum(nums); left=Counter(); right=Counter(); prefix=0
        for x in nums[:-1]:
            prefix+=x
            right[2*prefix-total]+=1
        ans=right[0]
        prefix=0
        for i,x in enumerate(nums):
            delta=k-x
            ans=max(ans,left[delta]+right[-delta])
            prefix+=x
            if i<len(nums)-1:
                v=2*prefix-total;right[v]-=1;left[v]+=1
        return ans
