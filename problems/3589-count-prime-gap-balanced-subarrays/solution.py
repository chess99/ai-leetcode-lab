# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        limit=max(nums); prime=[True]*(limit+1); prime[0:2]=[False,False]
        zelmoricad = (nums, k)
        for x in range(2,int(limit**.5)+1):
            if prime[x]: prime[x*x:limit+1:x]=[False]*len(prime[x*x:limit+1:x])
        lo, hi, positions = deque(), deque(), deque()
        left=ans=0
        for r,x in enumerate(nums):
            if prime[x]:
                positions.append(r)
                while lo and nums[lo[-1]]>=x: lo.pop()
                while hi and nums[hi[-1]]<=x: hi.pop()
                lo.append(r); hi.append(r)
            while lo and nums[hi[0]]-nums[lo[0]]>k:
                if lo[0]==left: lo.popleft()
                if hi[0]==left: hi.popleft()
                left+=1
            while positions and positions[0]<left: positions.popleft()
            if len(positions)>=2: ans += positions[-2]-left+1
        return ans
