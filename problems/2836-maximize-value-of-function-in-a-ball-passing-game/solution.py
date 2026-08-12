# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        size = len(receiver)
        levels = max(1, k.bit_length())
        jump = [receiver[:]]
        total = [receiver[:]]
        for _ in range(1, levels):
            previous_jump = jump[-1]
            previous_total = total[-1]
            jump.append([previous_jump[previous_jump[node]] for node in range(size)])
            total.append([previous_total[node]
                          + previous_total[previous_jump[node]]
                          for node in range(size)])
        answer = 0
        for start in range(size):
            node = start
            value = start
            remaining = k
            bit = 0
            while remaining:
                if remaining & 1:
                    value += total[bit][node]
                    node = jump[bit][node]
                remaining >>= 1
                bit += 1
            answer = max(answer, value)
        return answer
