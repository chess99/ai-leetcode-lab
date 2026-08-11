# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        balance = 0
        for char, is_locked in zip(s, locked):
            if is_locked == "0" or char == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        balance = 0
        for char, is_locked in zip(reversed(s), reversed(locked)):
            if is_locked == "0" or char == ")":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True
