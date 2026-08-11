# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:50:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        sequence = []
        def search(start: int) -> bool:
            if start == len(num): return len(sequence) >= 3
            value = 0
            for end in range(start, len(num)):
                if end > start and num[start] == "0": break
                value = value * 10 + int(num[end])
                if value > 2**31 - 1: break
                if len(sequence) >= 2:
                    expected = sequence[-1] + sequence[-2]
                    if value < expected: continue
                    if value > expected: break
                sequence.append(value)
                if search(end + 1): return True
                sequence.pop()
            return False
        return sequence if search(0) else []
