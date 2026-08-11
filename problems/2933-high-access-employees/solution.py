# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        groups = {}
        for name, time in access_times:
            groups.setdefault(name, []).append(int(time[:2]) * 60 + int(time[2:]))
        answer = []
        for name, times in groups.items():
            times.sort()
            if any(times[i + 2] - times[i] < 60 for i in range(len(times) - 2)):
                answer.append(name)
        return answer
