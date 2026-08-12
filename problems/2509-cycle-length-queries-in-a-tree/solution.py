# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        for first, second in queries:
            length = 1
            while first != second:
                if first > second:
                    first //= 2
                else:
                    second //= 2
                length += 1
            answer.append(length)
        return answer
