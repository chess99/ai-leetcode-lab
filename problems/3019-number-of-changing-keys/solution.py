# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(a.lower()!=b.lower() for a,b in zip(s,s[1:]))
