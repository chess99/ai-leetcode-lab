# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:13Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_count = Counter()
        answer = []
        for ball, color in queries:
            if ball in ball_color:
                old = ball_color[ball]
                color_count[old] -= 1
                if color_count[old] == 0:
                    del color_count[old]
            ball_color[ball] = color
            color_count[color] += 1
            answer.append(len(color_count))
        return answer
