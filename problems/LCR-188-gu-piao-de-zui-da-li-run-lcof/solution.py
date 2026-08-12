# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        minimum = float('inf')
        answer = 0
        for price in prices:
            minimum = min(minimum, price)
            answer = max(answer, price - minimum)
        return answer
