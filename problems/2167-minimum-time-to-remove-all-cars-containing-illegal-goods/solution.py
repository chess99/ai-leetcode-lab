# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumTime(self, s: str) -> int:
        answer = len(s)
        left_cost = 0
        for index, value in enumerate(s):
            left_cost = min(left_cost + 2 * (value == "1"), index + 1)
            answer = min(answer, left_cost + len(s) - index - 1)
        return answer
