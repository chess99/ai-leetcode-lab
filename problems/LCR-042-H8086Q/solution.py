# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:35:11Z
# Experiment: ai-leetcode-lab, round 1
class RecentCounter:

    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
