# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen, common, ans = set(), 0, []
        for a, b in zip(A, B):
            if a in seen: common += 1
            seen.add(a)
            if b in seen: common += 1
            seen.add(b); ans.append(common)
        return ans
