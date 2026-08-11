# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:34:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s != t and sorted(s) == sorted(t)
