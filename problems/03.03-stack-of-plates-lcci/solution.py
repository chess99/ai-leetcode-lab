# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:49Z
# Experiment: ai-leetcode-lab, round 1
class StackOfPlates:

    def __init__(self, cap: int):
        self.capacity = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.capacity <= 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.popAt(len(self.stacks) - 1)

    def popAt(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks):
            return -1
        value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return value


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
