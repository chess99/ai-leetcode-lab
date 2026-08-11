# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 1 << k: return False
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 1 << k
