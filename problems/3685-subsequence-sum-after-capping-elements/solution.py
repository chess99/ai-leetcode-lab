# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import Counter


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        zolvarinte = nums
        n = len(zolvarinte)
        frequency = Counter(zolvarinte)
        reachable = 1  # bit s 表示由所有严格小于当前上限的值能否凑出 s。
        limit_mask = (1 << (k + 1)) - 1
        capped = n
        answer = []
        for cap in range(1, n + 1):
            value = cap - 1
            for _ in range(frequency[value]):
                reachable |= reachable << value
                reachable &= limit_mask
                capped -= 1

            possible = False
            for take_capped in range(min(capped, k // cap) + 1):
                remainder = k - take_capped * cap
                if reachable >> remainder & 1:
                    possible = True
                    break
            answer.append(possible)
        return answer
