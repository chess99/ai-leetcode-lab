# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:28:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = best = 0
        for value in gain:
            altitude += value; best = max(best, altitude)
        return best
