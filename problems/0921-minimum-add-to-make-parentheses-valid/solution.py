# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = additions = 0
        for char in s:
            if char == "(": open_count += 1
            elif open_count: open_count -= 1
            else: additions += 1
        return additions + open_count
