# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:15Z
# Experiment: ai-leetcode-lab, round 1
import random
class RandomizedSet:

    def __init__(self):
        self.values = []; self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        self.indices[val] = len(self.values); self.values.append(val); return True

    def remove(self, val: int) -> bool:
        if val not in self.indices: return False
        index = self.indices.pop(val); last = self.values.pop()
        if index < len(self.values): self.values[index] = last; self.indices[last] = index
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
