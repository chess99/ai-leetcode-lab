# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:52Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        speed_sum = answer = 0
        for current_efficiency, current_speed in sorted(
                zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, current_speed)
            speed_sum += current_speed
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            answer = max(answer, speed_sum * current_efficiency)
        return answer % 1_000_000_007
