# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        gifts = [-gift for gift in gifts]; heapq.heapify(gifts)
        for _ in range(k): heapq.heapreplace(gifts, -int((-gifts[0]) ** 0.5))
        return -sum(gifts)
