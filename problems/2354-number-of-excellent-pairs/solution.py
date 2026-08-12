# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        cnt=[0]*31
        for x in set(nums):cnt[x.bit_count()]+=1
        return sum(cnt[i]*cnt[j] for i in range(31)for j in range(31)if i+j>=k)
