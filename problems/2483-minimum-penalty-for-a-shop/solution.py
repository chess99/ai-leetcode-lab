# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:22Z
# Experiment: ai-leetcode-lab, round 1

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        best_penalty = penalty
        best_hour = 0

        for hour, customer in enumerate(customers, start=1):
            if customer == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = hour

        return best_hour
