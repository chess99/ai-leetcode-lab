# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minimum = 0
        self.values = {}
        self.frequencies = {}
        self.groups = defaultdict(OrderedDict)

    def _touch(self, key):
        frequency = self.frequencies[key]
        del self.groups[frequency][key]
        if not self.groups[frequency] and self.minimum == frequency:
            self.minimum += 1
        self.frequencies[key] = frequency + 1
        self.groups[frequency + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key] = value
            self._touch(key)
            return
        if len(self.values) == self.capacity:
            removed, _ = self.groups[self.minimum].popitem(last=False)
            del self.values[removed]
            del self.frequencies[removed]
        self.values[key] = value
        self.frequencies[key] = 1
        self.groups[1][key] = None
        self.minimum = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
