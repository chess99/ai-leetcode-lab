# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        prefix = [[0, 0, 0]]
        for add in increase: prefix.append([prefix[-1][i] + add[i] for i in range(3)])
        answer = []
        for need in requirements:
            lo, hi = 0, len(prefix)
            while lo < hi:
                mid = (lo + hi) // 2
                if all(prefix[mid][i] >= need[i] for i in range(3)): hi = mid
                else: lo = mid + 1
            answer.append(lo if lo < len(prefix) else -1)
        return answer
