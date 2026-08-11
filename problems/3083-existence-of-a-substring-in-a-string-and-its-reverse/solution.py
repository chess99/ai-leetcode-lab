# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        return any(s[i : i + 2] in reversed_s for i in range(len(s) - 1))
