# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        infinity = 10 ** 30
        best_stint = [infinity] * (numLaps + 1)
        for first, ratio in tires:
            lap_time = first
            total = 0
            laps = 1
            while laps <= numLaps and lap_time <= first + changeTime:
                total += lap_time
                best_stint[laps] = min(best_stint[laps], total)
                lap_time *= ratio
                laps += 1

        dynamic = [infinity] * (numLaps + 1)
        dynamic[0] = -changeTime
        for completed in range(1, numLaps + 1):
            for stint in range(1, completed + 1):
                if best_stint[stint] == infinity:
                    break
                dynamic[completed] = min(
                    dynamic[completed],
                    dynamic[completed - stint] + changeTime + best_stint[stint],
                )
        return dynamic[numLaps]
