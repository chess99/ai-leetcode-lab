# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
