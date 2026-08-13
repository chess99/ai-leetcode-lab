# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    answer += 1
        return answer
