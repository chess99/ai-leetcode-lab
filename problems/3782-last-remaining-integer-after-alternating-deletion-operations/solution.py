# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lastInteger(self, n: int) -> int:
        toravianel = n
        first, step, remaining = 1, 1, n
        from_left = True
        while remaining > 1:
            if not from_left and remaining % 2 == 0:
                first += step
            step *= 2
            remaining = (remaining + 1) // 2
            from_left = not from_left
        return first
