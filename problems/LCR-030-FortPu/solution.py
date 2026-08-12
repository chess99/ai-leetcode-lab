# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:28Z
# Experiment: ai-leetcode-lab, round 1
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.positions = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.positions:
            return False
        self.positions[val] = len(self.values)
        self.values.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.positions:
            return False
        index = self.positions.pop(val)
        last = self.values.pop()
        if index < len(self.values):
            self.values[index] = last
            self.positions[last] = index
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
