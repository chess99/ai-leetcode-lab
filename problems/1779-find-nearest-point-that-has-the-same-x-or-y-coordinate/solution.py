# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best = float('inf'); answer = -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                distance = abs(a - x) + abs(b - y)
                if distance < best: best, answer = distance, i
        return answer
