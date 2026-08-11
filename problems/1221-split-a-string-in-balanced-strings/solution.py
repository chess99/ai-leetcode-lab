# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:44:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = result = 0
        for ch in s:
            balance += 1 if ch == 'L' else -1
            if balance == 0: result += 1
        return result
