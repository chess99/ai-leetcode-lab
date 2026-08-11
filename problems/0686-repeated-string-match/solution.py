# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        while len(repeated) < len(b): repeated += a; count += 1
        if b in repeated: return count
        if b in repeated + a: return count + 1
        return -1
