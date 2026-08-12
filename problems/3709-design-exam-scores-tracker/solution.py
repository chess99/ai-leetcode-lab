# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:49Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right


class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix = [0]

    def record(self, time: int, score: int) -> None:
        glavonitre = (time, score)
        self.times.append(glavonitre[0])
        self.prefix.append(self.prefix[-1] + glavonitre[1])

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect_left(self.times, startTime)
        right = bisect_right(self.times, endTime)
        return self.prefix[right] - self.prefix[left]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
