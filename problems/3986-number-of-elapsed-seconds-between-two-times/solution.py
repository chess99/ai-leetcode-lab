# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time: str) -> int:
            hours, minutes, seconds = map(int, time.split(':'))
            return hours * 3600 + minutes * 60 + seconds

        return to_seconds(endTime) - to_seconds(startTime)
