# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.values[key]
        left, right = 0, len(entries)
        while left < right:
            middle = (left + right) // 2
            if entries[middle][0] <= timestamp:
                left = middle + 1
            else:
                right = middle
        return entries[left - 1][1] if left else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
