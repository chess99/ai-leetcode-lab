# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:45Z
# Experiment: ai-leetcode-lab, round 1
class IntervalNode:
    __slots__ = ("left", "right", "priority", "smaller", "larger")

    def __init__(self, left, right, priority):
        self.left = left
        self.right = right
        self.priority = priority
        self.smaller = None
        self.larger = None


class CountIntervals:

    def __init__(self):
        self.root = None
        self.covered = 0
        self.seed = 1

    def _priority(self):
        self.seed = (self.seed * 1103515245 + 12345) & 0x7fffffff
        return self.seed

    def _split(self, node, key):
        if node is None:
            return None, None
        if node.left < key:
            first, second = self._split(node.larger, key)
            node.larger = first
            return node, second
        first, second = self._split(node.smaller, key)
        node.smaller = second
        return first, node

    def _merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.priority > second.priority:
            first.larger = self._merge(first.larger, second)
            return first
        second.smaller = self._merge(first, second.smaller)
        return second

    def _pop_largest(self, node):
        if node.larger is None:
            remainder = node.smaller
            node.smaller = None
            return remainder, node
        node.larger, largest = self._pop_largest(node.larger)
        return node, largest

    def _pop_smallest(self, node):
        if node.smaller is None:
            remainder = node.larger
            node.larger = None
            return remainder, node
        node.smaller, smallest = self._pop_smallest(node.smaller)
        return node, smallest

    def add(self, left: int, right: int) -> None:
        smaller, larger = self._split(self.root, left)
        if smaller is not None:
            smaller, predecessor = self._pop_largest(smaller)
            if predecessor.right + 1 >= left:
                left = predecessor.left
                right = max(right, predecessor.right)
                self.covered -= predecessor.right - predecessor.left + 1
            else:
                smaller = self._merge(smaller, predecessor)

        while larger is not None:
            larger, successor = self._pop_smallest(larger)
            if successor.left > right + 1:
                larger = self._merge(successor, larger)
                break
            right = max(right, successor.right)
            self.covered -= successor.right - successor.left + 1

        interval = IntervalNode(left, right, self._priority())
        self.root = self._merge(self._merge(smaller, interval), larger)
        self.covered += right - left + 1

    def count(self) -> int:
        return self.covered


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
