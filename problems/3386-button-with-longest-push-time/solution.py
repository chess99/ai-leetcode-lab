# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest = -1
        button = float("inf")
        previous_time = 0

        for index, time in events:
            duration = time - previous_time
            if duration > longest or (duration == longest and index < button):
                longest = duration
                button = index
            previous_time = time

        return button
