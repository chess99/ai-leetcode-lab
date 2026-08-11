# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        size = 1 << n
        palindrome_length = [0] * size

        for mask in range(1, size):
            chosen = [s[i] for i in range(n) if mask & (1 << i)]
            if chosen == chosen[::-1]:
                palindrome_length[mask] = len(chosen)

        best_submask = palindrome_length[:]
        for bit in range(n):
            for mask in range(size):
                if mask & (1 << bit):
                    best_submask[mask] = max(
                        best_submask[mask], best_submask[mask ^ (1 << bit)]
                    )

        full_mask = size - 1
        answer = 0
        for first in range(size):
            answer = max(answer, palindrome_length[first] * best_submask[full_mask ^ first])

        return answer
