# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root={};ans=0
        for w in words:
            node=root
            for a,b in zip(w,reversed(w)):
                node=node.setdefault((a,b),{})
                ans+=node.get(None,0)
            node[None]=node.get(None,0)+1
        return ans
