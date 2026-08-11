# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        best = total = job_index = 0
        for ability in sorted(worker):
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                best = max(best, jobs[job_index][1])
                job_index += 1
            total += best
        return total
