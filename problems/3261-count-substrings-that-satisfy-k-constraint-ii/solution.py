# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:33Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        minimum_left = [0] * n
        prefix = [0] * (n + 1)
        counts = [0, 0]
        left = 0

        for right, char in enumerate(s):
            counts[ord(char) - ord('0')] += 1
            while counts[0] > k and counts[1] > k:
                counts[ord(s[left]) - ord('0')] -= 1
                left += 1
            minimum_left[right] = left
            prefix[right + 1] = prefix[right] + right - left + 1

        answer = []
        for query_left, query_right in queries:
            split = bisect_left(minimum_left, query_left, query_left, query_right + 1)
            full_width = split - query_left
            total = full_width * (full_width + 1) // 2
            total += prefix[query_right + 1] - prefix[split]
            answer.append(total)
        return answer
