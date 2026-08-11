# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:40Z
# Experiment: ai-leetcode-lab, round 1
class MyCalendarTwo:

    def __init__(self):
        self.bookings, self.overlaps = [], []

    def book(self, startTime: int, endTime: int) -> bool:
        if any(startTime < end and start < endTime for start, end in self.overlaps): return False
        for start, end in self.bookings:
            if startTime < end and start < endTime: self.overlaps.append((max(start, startTime), min(end, endTime)))
        self.bookings.append((startTime, endTime)); return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
