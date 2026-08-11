# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        window = sum(gaps[:k + 1])
        answer = window
        for i in range(k + 1, len(gaps)):
            window += gaps[i] - gaps[i - k - 1]
            answer = max(answer, window)
        return answer
