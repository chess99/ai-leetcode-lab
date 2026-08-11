# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:18Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        answer=0
        for i in range(len(nums)):
            current=0
            for x in nums[i:]:
                current=gcd(current,x)
                if current==k: answer+=1
                if current<k or current%k: break
        return answer
