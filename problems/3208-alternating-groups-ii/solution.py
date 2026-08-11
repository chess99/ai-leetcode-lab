# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        run = 1
        answer = 0
        for index in range(1, length + k - 1):
            if colors[index % length] != colors[(index - 1) % length]:
                run += 1
            else:
                run = 1
            if run >= k:
                answer += 1
        return answer
