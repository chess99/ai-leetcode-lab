# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:58Z
# Experiment: ai-leetcode-lab, round 1
class StreamRank:

    def __init__(self):
        self.values = []

    def track(self, x: int) -> None:
        from bisect import insort
        insort(self.values, x)

    def getRankOfNumber(self, x: int) -> int:
        from bisect import bisect_right
        return bisect_right(self.values, x)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
