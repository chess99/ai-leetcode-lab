# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)
