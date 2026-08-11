# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in parent]
        for node in range(1, len(parent)):
            self.children[parent[node]].append(node)
        self.locked_by = [0] * len(parent)

    def lock(self, num: int, user: int) -> bool:
        if self.locked_by[num] != 0:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked_by[num] != 0:
            return False

        ancestor = self.parent[num]
        while ancestor != -1:
            if self.locked_by[ancestor] != 0:
                return False
            ancestor = self.parent[ancestor]

        locked_descendants = []
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.locked_by[node] != 0:
                locked_descendants.append(node)
            stack.extend(self.children[node])

        if not locked_descendants:
            return False

        for node in locked_descendants:
            self.locked_by[node] = 0
        self.locked_by[num] = user
        return True
