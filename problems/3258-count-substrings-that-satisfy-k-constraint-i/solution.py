# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:48:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        return sum(s[i:j].count('0')<=k or s[i:j].count('1')<=k for i in range(len(s)) for j in range(i+1,len(s)+1))
