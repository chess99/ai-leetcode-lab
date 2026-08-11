# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.front_half = deque()
        self.back_half = deque()

    def _rebalance(self) -> None:
        if len(self.front_half) > len(self.back_half) + 1:
            self.back_half.appendleft(self.front_half.pop())
        elif len(self.front_half) < len(self.back_half):
            self.front_half.append(self.back_half.popleft())

    def pushFront(self, val: int) -> None:
        self.front_half.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front_half) > len(self.back_half):
            self.back_half.appendleft(self.front_half.pop())
        self.front_half.append(val)

    def pushBack(self, val: int) -> None:
        self.back_half.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.front_half:
            return -1
        value = self.front_half.popleft()
        self._rebalance()
        return value

    def popMiddle(self) -> int:
        if not self.front_half:
            return -1
        value = self.front_half.pop()
        self._rebalance()
        return value

    def popBack(self) -> int:
        if not self.front_half:
            return -1
        if self.back_half:
            value = self.back_half.pop()
        else:
            value = self.front_half.pop()
        self._rebalance()
        return value
