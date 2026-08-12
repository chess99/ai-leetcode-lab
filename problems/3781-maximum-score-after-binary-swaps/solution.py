# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        banterisol = (nums, s)
        available = []
        answer = 0
        # 到达一个原始 1 时，至今必须放置的 1 数增加；选前缀中最大权值位置。
        for value, bit in zip(*banterisol):
            heapq.heappush(available, -value)
            if bit == '1':
                answer -= heapq.heappop(available)
        return answer
