# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:19Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = Counter(ages)
        total = 0
        for sender in range(1, 121):
            for receiver in range(1, 121):
                if receiver > sender / 2 + 7 and receiver <= sender:
                    total += counts[sender] * (counts[receiver] - (sender == receiver))
        return total
