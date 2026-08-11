# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [q for q in queries if any(sum(a!=b for a,b in zip(q,d))<=2 for d in dictionary)]
