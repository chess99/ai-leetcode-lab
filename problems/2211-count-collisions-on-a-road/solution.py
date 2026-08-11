# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:16Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def countCollisions(self, directions: str) -> int:
        relevant = directions.lstrip("L").rstrip("R")
        return sum(direction != "S" for direction in relevant)
