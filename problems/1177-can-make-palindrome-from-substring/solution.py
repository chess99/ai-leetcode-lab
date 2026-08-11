# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix=[0]
        for ch in s: prefix.append(prefix[-1] ^ (1 << (ord(ch)-97)))
        return [((prefix[r+1]^prefix[l]).bit_count()//2 <= k) for l,r,k in queries]
