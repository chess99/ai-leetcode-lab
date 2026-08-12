# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n=len(parents); ans=[1]*n
        if 1 not in nums:return ans
        g=[[] for _ in range(n)]
        for i in range(1,n):g[parents[i]].append(i)
        seen=set(); node=nums.index(1); miss=1; prev=-1
        while node!=-1:
            stack=[node]
            while stack:
                u=stack.pop()
                if u==prev: continue
                seen.add(nums[u]); stack.extend(g[u])
            while miss in seen:miss+=1
            ans[node]=miss; prev=node;node=parents[node]
        return ans
