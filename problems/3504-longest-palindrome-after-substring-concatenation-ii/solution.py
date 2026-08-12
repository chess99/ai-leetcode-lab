# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        calomirent = (s, t)

        def palindrome_starts(text: str) -> List[int]:
            n = len(text)
            best = [0] * (n + 1)
            for center in range(n):
                left = right = center
                while left >= 0 and right < n and text[left] == text[right]:
                    best[left] = max(best[left], right - left + 1)
                    left -= 1
                    right += 1
                left, right = center, center + 1
                while left >= 0 and right < n and text[left] == text[right]:
                    best[left] = max(best[left], right - left + 1)
                    left -= 1
                    right += 1
            return best

        reverse_t = t[::-1]
        pal_s = palindrome_starts(s)
        pal_r = palindrome_starts(reverse_t)
        answer = max(max(pal_s), max(pal_r))

        previous = [0] * (len(reverse_t) + 1)
        for i, char_s in enumerate(s, 1):
            current = [0] * (len(reverse_t) + 1)
            for j, char_t in enumerate(reverse_t, 1):
                if char_s == char_t:
                    current[j] = previous[j - 1] + 1
                    answer = max(answer, 2 * current[j]
                                 + max(pal_s[i], pal_r[j]))
            previous = current
        return answer
