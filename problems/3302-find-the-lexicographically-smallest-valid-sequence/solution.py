# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        positions = [[] for _ in range(26)]
        for i, char in enumerate(word1):
            positions[ord(char) - ord('a')].append(i)
        def previous(limit: int, char: str) -> int:
            indices = positions[ord(char) - ord('a')]
            at = bisect_left(indices, limit) - 1
            return indices[at] if at >= 0 else -1

        exact = [-1] * (m + 1)
        one_error = [-1] * (m + 1)
        exact[m] = one_error[m] = n
        for j in range(m - 1, -1, -1):
            exact[j] = previous(exact[j + 1], word2[j]) if exact[j + 1] >= 0 else -1
            matched = previous(one_error[j + 1], word2[j]) if one_error[j + 1] >= 0 else -1
            changed = exact[j + 1] - 1 if exact[j + 1] >= 0 else -1
            one_error[j] = max(matched, changed)
        answer = []
        used_mismatch = False
        j = 0
        for i, char in enumerate(word1):
            if j == m:
                break
            if char == word2[j] and (exact[j + 1] > i if used_mismatch else one_error[j + 1] > i):
                answer.append(i)
                j += 1
            elif not used_mismatch and exact[j + 1] > i:
                answer.append(i)
                used_mismatch = True
                j += 1
        return answer
