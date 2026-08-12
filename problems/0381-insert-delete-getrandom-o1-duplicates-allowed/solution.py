# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:14Z
# Experiment: ai-leetcode-lab, round 1
import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        absent = not self.positions[val]
        self.positions[val].add(len(self.values))
        self.values.append(val)
        return absent

    def remove(self, val: int) -> bool:
        if not self.positions[val]:
            return False
        remove_index = self.positions[val].pop()
        last = self.values[-1]
        if remove_index != len(self.values) - 1:
            self.values[remove_index] = last
            self.positions[last].remove(len(self.values) - 1)
            self.positions[last].add(remove_index)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
