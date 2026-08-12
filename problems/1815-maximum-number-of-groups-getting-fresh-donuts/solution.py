# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:46Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        counts = Counter(group % batchSize for group in groups)
        answer = counts[0]
        for remainder in range(1, (batchSize + 1) // 2):
            pairs = min(counts[remainder], counts[batchSize - remainder])
            answer += pairs
            counts[remainder] -= pairs
            counts[batchSize - remainder] -= pairs
        if batchSize % 2 == 0:
            pairs = counts[batchSize // 2] // 2
            answer += pairs
            counts[batchSize // 2] -= pairs * 2
        state = tuple(counts[remainder] for remainder in range(1, batchSize))

        @lru_cache(None)
        def search(state, remainder):
            best = 0
            for index, count in enumerate(state):
                if count == 0:
                    continue
                following = list(state)
                following[index] -= 1
                best = max(best, int(remainder == 0) +
                           search(tuple(following),
                                  (remainder + index + 1) % batchSize))
            return best

        return answer + search(state, 0)
