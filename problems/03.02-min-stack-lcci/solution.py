# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:56:58Z
# Experiment: ai-leetcode-lab, round 1
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.minimums = []

    def push(self, x: int) -> None:
        self.values.append(x)
        self.minimums.append(min(x, self.minimums[-1]) if self.minimums else x)

    def pop(self) -> None:
        self.values.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
