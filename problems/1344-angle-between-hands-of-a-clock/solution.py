# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:15Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        difference = abs(hour_angle - minute_angle)
        return min(difference, 360 - difference)
