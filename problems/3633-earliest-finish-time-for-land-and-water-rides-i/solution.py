# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:07:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = float("inf")
        for land_start, land_length in zip(landStartTime, landDuration):
            land_finish = land_start + land_length
            for water_start, water_length in zip(waterStartTime, waterDuration):
                water_finish = water_start + water_length
                answer = min(
                    answer,
                    max(land_finish, water_start) + water_length,
                    max(water_finish, land_start) + land_length,
                )
        return int(answer)
