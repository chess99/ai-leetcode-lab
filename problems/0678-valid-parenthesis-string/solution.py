# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:30:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkValidString(self, s: str) -> bool:
        lowest_open = 0
        highest_open = 0
        for char in s:
            if char == "(":
                lowest_open += 1
                highest_open += 1
            elif char == ")":
                lowest_open = max(0, lowest_open - 1)
                highest_open -= 1
            else:
                lowest_open = max(0, lowest_open - 1)
                highest_open += 1
            if highest_open < 0:
                return False
        return lowest_open == 0
