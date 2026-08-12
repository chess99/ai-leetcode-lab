# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:41Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        hasturvane = (landStartTime, landDuration, waterStartTime, waterDuration)

        def prepare(starts, durations):
            rides = sorted(zip(starts, durations))
            ordered_starts = [start for start, _ in rides]
            prefix_duration = []
            best = float('inf')
            for _, duration in rides:
                best = min(best, duration)
                prefix_duration.append(best)
            suffix_finish = [0] * len(rides)
            best = float('inf')
            for i in range(len(rides) - 1, -1, -1):
                best = min(best, rides[i][0] + rides[i][1])
                suffix_finish[i] = best
            return ordered_starts, prefix_duration, suffix_finish

        def finish_after(time, prepared):
            starts, prefix_duration, suffix_finish = prepared
            split = bisect_right(starts, time)
            answer = float('inf')
            if split:
                answer = time + prefix_duration[split - 1]
            if split < len(starts):
                answer = min(answer, suffix_finish[split])
            return answer

        land = prepare(landStartTime, landDuration)
        water = prepare(waterStartTime, waterDuration)
        answer = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            answer = min(answer, finish_after(start + duration, water))
        for start, duration in zip(waterStartTime, waterDuration):
            answer = min(answer, finish_after(start + duration, land))
        return answer
