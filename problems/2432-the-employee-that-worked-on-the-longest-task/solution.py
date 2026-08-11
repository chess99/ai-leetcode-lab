# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        answer, longest, previous = logs[0][0], logs[0][1], 0
        for employee, end in logs:
            duration = end - previous
            if duration > longest or (duration == longest and employee < answer):
                answer, longest = employee, duration
            previous = end
        return answer
