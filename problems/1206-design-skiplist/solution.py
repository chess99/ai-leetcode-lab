# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:11Z
# Experiment: ai-leetcode-lab, round 1
import random


class Node:
    def __init__(self, value: int, level: int):
        self.value = value
        self.next = [None] * level


class Skiplist:

    def __init__(self):
        self.maximum_level = 16
        self.head = Node(-1, self.maximum_level)

    def _predecessors(self, target: int):
        update = [self.head] * self.maximum_level
        current = self.head
        for level in range(self.maximum_level - 1, -1, -1):
            while current.next[level] and current.next[level].value < target:
                current = current.next[level]
            update[level] = current
        return update

    def search(self, target: int) -> bool:
        following = self._predecessors(target)[0].next[0]
        return following is not None and following.value == target

    def add(self, num: int) -> None:
        update = self._predecessors(num)
        level = 1
        while level < self.maximum_level and random.getrandbits(1):
            level += 1
        node = Node(num, level)
        for current_level in range(level):
            node.next[current_level] = update[current_level].next[current_level]
            update[current_level].next[current_level] = node

    def erase(self, num: int) -> bool:
        update = self._predecessors(num)
        target = update[0].next[0]
        if target is None or target.value != num:
            return False
        for level in range(len(target.next)):
            if update[level].next[level] is target:
                update[level].next[level] = target.next[level]
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
