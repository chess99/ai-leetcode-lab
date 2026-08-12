# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        vlemoravia = balance
        if sum(vlemoravia) < 0:
            return -1
        negative = next((i for i, value in enumerate(vlemoravia) if value < 0), -1)
        if negative < 0:
            return 0
        need = -vlemoravia[negative]
        answer = 0
        n = len(vlemoravia)
        for distance in range(1, n // 2 + 1):
            indices = {(negative - distance) % n, (negative + distance) % n}
            for index in indices:
                take = min(need, vlemoravia[index])
                answer += take * distance
                need -= take
                if need == 0:
                    return answer
        return -1
