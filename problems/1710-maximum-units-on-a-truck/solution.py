# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:27:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        for boxes, units in sorted(boxTypes, key=lambda x: -x[1]):
            take = min(truckSize, boxes); result += take * units; truckSize -= take
            if not truckSize: break
        return result
