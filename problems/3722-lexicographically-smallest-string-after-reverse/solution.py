# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        for k in range(1, len(s) + 1):
            ans = min(ans, s[:k][::-1] + s[k:], s[:-k] + s[-k:][::-1])
        return ans
