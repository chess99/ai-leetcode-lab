# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def ordinal(date):
            month, day = map(int, date.split('-'))
            return sum(days[:month - 1]) + day
        return max(0, min(ordinal(leaveAlice), ordinal(leaveBob)) - max(ordinal(arriveAlice), ordinal(arriveBob)) + 1)
