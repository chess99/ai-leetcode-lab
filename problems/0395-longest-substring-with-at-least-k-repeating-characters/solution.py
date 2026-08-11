# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:return 0
        for c in set(s):
            if s.count(c)<k:return max(map(lambda part:self.longestSubstring(part,k),s.split(c)))
        return len(s)
