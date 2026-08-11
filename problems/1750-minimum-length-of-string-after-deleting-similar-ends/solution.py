# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            character = s[left]
            while left <= right and s[left] == character:
                left += 1
            while left <= right and s[right] == character:
                right -= 1

        return right - left + 1
