# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(text, left, right):
            while left < right:
                if text[left] != text[right]:
                    return False
                left += 1
                right -= 1
            return True

        def check(first, second):
            left, right = 0, len(first) - 1
            while left < right and first[left] == second[right]:
                left += 1
                right -= 1
            return is_palindrome(first, left, right) or is_palindrome(
                second, left, right
            )

        return check(a, b) or check(b, a)
