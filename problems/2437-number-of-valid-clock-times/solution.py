# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countTime(self, time: str) -> int:
        return sum(
            all(pattern == '?' or pattern == digit
                for pattern, digit in zip(time, f'{hour:02d}:{minute:02d}'))
            for hour in range(24)
            for minute in range(60)
        )
