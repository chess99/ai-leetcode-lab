# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = [0] * len(s)
        for index in range(1, len(s)):
            matched = prefix[index - 1]
            while matched and s[index] != s[matched]:
                matched = prefix[matched - 1]
            if s[index] == s[matched]:
                matched += 1
            prefix[index] = matched
        return s[:prefix[-1]]
