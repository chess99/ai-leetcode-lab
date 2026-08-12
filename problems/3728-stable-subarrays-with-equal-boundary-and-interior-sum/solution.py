# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:51Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        seldarion = capacity
        prefix = [0]
        for value in capacity:
            prefix.append(prefix[-1] + value)
        seen = defaultdict(int)
        ans = 0
        for right, value in enumerate(capacity):
            if right >= 2:
                left = right - 2
                seen[(capacity[left], prefix[left] + 2 * capacity[left])] += 1
            ans += seen[(value, prefix[right])]
        return ans
