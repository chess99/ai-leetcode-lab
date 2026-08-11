# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:35:11Z
# Experiment: ai-leetcode-lab, round 1
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.values = []
        self.start = 0
        self.total = 0
    def next(self, val: int) -> float:
        self.values.append(val)
        self.total += val
        if len(self.values) - self.start > self.size:
            self.total -= self.values[self.start]
            self.start += 1
        return self.total / (len(self.values) - self.start)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
