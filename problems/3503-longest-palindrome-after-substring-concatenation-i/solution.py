# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans = 0
        a = [s[i:j] for i in range(len(s) + 1) for j in range(i, len(s) + 1)]
        b = [t[i:j] for i in range(len(t) + 1) for j in range(i, len(t) + 1)]
        for left in a:
            for right in b:
                candidate = left + right
                if len(candidate) > ans and candidate == candidate[::-1]:
                    ans = len(candidate)
        return ans
