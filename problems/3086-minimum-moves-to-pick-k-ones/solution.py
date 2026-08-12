# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos=[i for i,x in enumerate(nums) if x]
        consecutive = 0
        for index in range(len(nums)):
            consecutive = max(consecutive,
                              nums[index]
                              + (nums[index - 1] if index else 0)
                              + (nums[index + 1] if index + 1 < len(nums) else 0))
        take = max(0, k - maxChanges)
        if take <= min(consecutive, k):
            take = min(consecutive, k)
            return take - (1 if take else 0) + 2 * (k - take)
        pre=[0]
        for x in pos:pre.append(pre[-1]+x)
        best=10**18
        for l in range(len(pos)-take+1):
            r=l+take-1;m=(l+r)//2
            move=pos[m]*(m-l)-(pre[m]-pre[l])+(pre[r+1]-pre[m+1])-pos[m]*(r-m)
            best=min(best,move+2*(k-take))
        return best
