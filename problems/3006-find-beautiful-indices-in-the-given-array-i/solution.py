# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def positions(word: str) -> List[int]:
            return [i for i in range(len(s) - len(word) + 1) if s.startswith(word, i)]

        a_positions = positions(a)
        b_positions = positions(b)
        answer = []
        for i in a_positions:
            index = bisect_left(b_positions, i)
            if (index < len(b_positions) and b_positions[index] - i <= k) or (
                index > 0 and i - b_positions[index - 1] <= k
            ):
                answer.append(i)
        return answer
