# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:21:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(a)-int(b)) <= 2 for a,b in zip(s,s[1:]))
