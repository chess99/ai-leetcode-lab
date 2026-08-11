# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:17Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = (intLength + 1) // 2
        first_half = 10 ** (half_length - 1)
        limit = 10**half_length
        answer = []

        for query in queries:
            prefix = first_half + query - 1
            if prefix >= limit:
                answer.append(-1)
                continue

            text = str(prefix)
            if intLength % 2:
                answer.append(int(text + text[-2::-1]))
            else:
                answer.append(int(text + text[::-1]))

        return answer
