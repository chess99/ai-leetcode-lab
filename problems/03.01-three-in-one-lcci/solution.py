# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:56:58Z
# Experiment: ai-leetcode-lab, round 1
class TripleInOne:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.stacks = [[] for _ in range(3)]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stacks[stackNum]) < self.size:
            self.stacks[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        return self.stacks[stackNum].pop() if self.stacks[stackNum] else -1

    def peek(self, stackNum: int) -> int:
        return self.stacks[stackNum][-1] if self.stacks[stackNum] else -1

    def isEmpty(self, stackNum: int) -> bool:
        return not self.stacks[stackNum]


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
