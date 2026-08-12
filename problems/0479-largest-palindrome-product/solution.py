# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for left in range(upper, lower - 1, -1):
            palindrome = int(str(left) + str(left)[::-1])
            factor = upper
            while factor * factor >= palindrome:
                if palindrome % factor == 0:
                    return palindrome % 1337
                factor -= 1
        return 0
