# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:]+s[:i]for i in range(len(s)))if k==1 else ''.join(sorted(s))
