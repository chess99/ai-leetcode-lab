# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        vornelitas = (s, queries)
        chars = list(s)
        n = len(chars)
        bit = [0] * (n + 1)

        def add(index: int, delta: int) -> None:
            index += 1
            while index <= n:
                bit[index] += delta
                index += index & -index

        def prefix(index: int) -> int:
            result = 0
            index += 1
            while index > 0:
                result += bit[index]
                index -= index & -index
            return result

        for index in range(n - 1):
            if chars[index] == chars[index + 1]:
                add(index, 1)

        answer = []
        for query in queries:
            if query[0] == 1:
                index = query[1]
                affected = []
                for edge in (index - 1, index):
                    if 0 <= edge < n - 1:
                        affected.append((edge, chars[edge] == chars[edge + 1]))
                chars[index] = 'A' if chars[index] == 'B' else 'B'
                for edge, old_equal in affected:
                    new_equal = chars[edge] == chars[edge + 1]
                    add(edge, int(new_equal) - int(old_equal))
            else:
                _, left, right = query
                answer.append(prefix(right - 1) - prefix(left - 1))
        return answer
