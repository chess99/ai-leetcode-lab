# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:56Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        size = len(s)
        palindromes = [[False] * size for _ in range(size)]
        for left in range(size - 1, -1, -1):
            palindromes[left][left] = True
            for right in range(left + 1, size):
                palindromes[left][right] = (s[left] == s[right]
                                             and (right - left == 1
                                                  or palindromes[left + 1][right - 1]))
        dynamic = [0] * (size + 1)
        for end in range(1, size + 1):
            dynamic[end] = dynamic[end - 1]
            for length in (k, k + 1):
                start = end - length
                if start >= 0 and palindromes[start][end - 1]:
                    dynamic[end] = max(dynamic[end], dynamic[start] + 1)
        return dynamic[size]
