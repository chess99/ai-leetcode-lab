# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:50Z
# Experiment: ai-leetcode-lab, round 1
class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        temporary = []
        while self.stack and self.stack[-1] < val:
            temporary.append(self.stack.pop())
        self.stack.append(val)
        while temporary:
            self.stack.append(temporary.pop())

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1] if self.stack else -1

    def isEmpty(self) -> bool:
        return not self.stack


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
