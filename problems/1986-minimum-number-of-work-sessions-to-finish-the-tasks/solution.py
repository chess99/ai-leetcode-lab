# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        task_count = len(tasks)
        best = [(task_count + 1, 0)] * (1 << task_count)
        best[0] = (1, 0)

        for mask in range(1 << task_count):
            sessions, used_time = best[mask]
            for task_index, duration in enumerate(tasks):
                if mask & (1 << task_index):
                    continue
                next_mask = mask | (1 << task_index)
                if used_time + duration <= sessionTime:
                    candidate = (sessions, used_time + duration)
                else:
                    candidate = (sessions + 1, duration)
                best[next_mask] = min(best[next_mask], candidate)

        return best[-1][0]
