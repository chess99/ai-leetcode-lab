# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:26:52Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks).values()
        maximum = max(frequencies)
        maximum_count = sum(count == maximum for count in frequencies)
        return max(len(tasks), (maximum - 1) * (n + 1) + maximum_count)
