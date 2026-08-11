# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for percentage in batteryPercentages:
            if percentage > tested:
                tested += 1
        return tested
