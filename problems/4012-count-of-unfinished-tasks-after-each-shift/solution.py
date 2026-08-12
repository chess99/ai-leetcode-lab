# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from bisect import bisect_right


class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        drelvanito = (tasks, shifts)
        prefix = []
        total = 0
        for task in tasks:
            total += task
            prefix.append(total)

        progress = 0
        answer = []
        for shift in shifts:
            if shift >= total - progress:
                progress = 0
                answer.append(0)
                continue
            progress += shift
            completed = bisect_right(prefix, progress)
            answer.append(len(tasks) - completed)
        return answer
