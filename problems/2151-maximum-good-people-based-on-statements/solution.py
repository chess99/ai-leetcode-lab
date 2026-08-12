# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        size = len(statements)
        answer = 0
        for mask in range(1 << size):
            valid = True
            for person in range(size):
                if not (mask >> person) & 1:
                    continue
                for target, statement in enumerate(statements[person]):
                    if statement != 2 and statement != ((mask >> target) & 1):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                answer = max(answer, mask.bit_count())
        return answer
