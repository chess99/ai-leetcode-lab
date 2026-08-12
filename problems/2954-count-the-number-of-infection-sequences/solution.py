# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        modulus = 10 ** 9 + 7
        healthy = n - len(sick)
        factorial = [1] * (healthy + 1)
        for value in range(1, healthy + 1):
            factorial[value] = factorial[value - 1] * value % modulus
        gaps = [sick[0], n - 1 - sick[-1]]
        internal = []
        for first, second in zip(sick, sick[1:]):
            gap = second - first - 1
            gaps.append(gap)
            if gap:
                internal.append(gap)
        answer = factorial[healthy]
        for gap in gaps:
            answer = answer * pow(factorial[gap], modulus - 2, modulus) % modulus
        answer = answer * pow(2, sum(gap - 1 for gap in internal), modulus) % modulus
        return answer
