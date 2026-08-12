# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        from bisect import bisect_left
        n=len(nums)//2; total=sum(nums); a=nums[:n];b=nums[n:]
        left=[[] for _ in range(n+1)];right=[[] for _ in range(n+1)]
        for mask in range(1<<n):
            c=mask.bit_count(); left[c].append(sum(a[i] for i in range(n) if mask>>i&1));right[c].append(sum(b[i] for i in range(n) if mask>>i&1))
        ans=float('inf')
        for c in range(n+1):
            right[n-c].sort()
            for x in left[c]:
                j=bisect_left(right[n-c],total/2-x)
                for t in (j-1,j):
                    if 0<=t<len(right[n-c]):ans=min(ans,abs(total-2*(x+right[n-c][t])))
        return ans
