# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n,total=len(nums),sum(nums); possible=[set() for _ in range(n//2+1)];possible[0].add(0)
        for value in nums:
            for count in range(n//2,0,-1):
                possible[count].update(previous+value for previous in possible[count-1])
        return any(total*count%n==0 and total*count//n in possible[count] for count in range(1,n//2+1))
