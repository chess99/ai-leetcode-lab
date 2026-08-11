# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:32:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(set(s[index:index+3]))==3 for index in range(len(s)-2))
