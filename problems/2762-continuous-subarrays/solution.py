# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        lo, hi = deque(), deque(); left=ans=0
        for right,x in enumerate(nums):
            while lo and nums[lo[-1]]>x: lo.pop()
            while hi and nums[hi[-1]]<x: hi.pop()
            lo.append(right); hi.append(right)
            while nums[hi[0]]-nums[lo[0]]>2:
                if lo[0]==left: lo.popleft()
                if hi[0]==left: hi.popleft()
                left+=1
            ans+=right-left+1
        return ans
