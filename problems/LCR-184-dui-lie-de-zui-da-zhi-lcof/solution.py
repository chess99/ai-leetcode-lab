# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Checkout:

    def __init__(self):
        self.queue = deque()
        self.maximums = deque()

    def get_max(self) -> int:
        return self.maximums[0] if self.maximums else -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        while self.maximums and self.maximums[-1] < value:
            self.maximums.pop()
        self.maximums.append(value)

    def remove(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.popleft()
        if value == self.maximums[0]:
            self.maximums.popleft()
        return value


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
