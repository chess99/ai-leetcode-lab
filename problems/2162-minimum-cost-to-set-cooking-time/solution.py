# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minimum_cost = float("inf")

        for minutes in range(100):
            seconds = targetSeconds - 60 * minutes
            if not 0 <= seconds <= 99:
                continue

            digits = f"{minutes:02d}{seconds:02d}".lstrip("0")
            finger = startAt
            cost = 0

            for char in digits:
                digit = int(char)
                if digit != finger:
                    cost += moveCost
                    finger = digit
                cost += pushCost

            minimum_cost = min(minimum_cost, cost)

        return minimum_cost
