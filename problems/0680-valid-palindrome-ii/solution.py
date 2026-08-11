# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:58:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left, right = left + 1, right - 1
        return True
