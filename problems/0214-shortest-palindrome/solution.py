# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        joined = s + "#" + s[::-1]; prefix = [0] * len(joined)
        for i in range(1, len(joined)):
            j = prefix[i - 1]
            while j and joined[i] != joined[j]: j = prefix[j - 1]
            if joined[i] == joined[j]: j += 1
            prefix[i] = j
        return s[prefix[-1]:][::-1] + s
