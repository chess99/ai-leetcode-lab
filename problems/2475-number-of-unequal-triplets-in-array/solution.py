# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts={}
        for value in nums:counts[value]=counts.get(value,0)+1
        left=answer=0
        for count in counts.values():answer+=left*count*(len(nums)-left-count);left+=count
        return answer
