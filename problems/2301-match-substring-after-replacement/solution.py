# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mp={}
        for a,b in mappings:mp.setdefault(a,set()).add(b)
        return any(all(x==y or x in mp.get(y,set()) for x,y in zip(s[i:i+len(sub)],sub)) for i in range(len(s)-len(sub)+1))
