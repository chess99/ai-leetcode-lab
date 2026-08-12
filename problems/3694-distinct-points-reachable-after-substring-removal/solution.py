# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        delta = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        x = y = 0
        prefix = [(0, 0)]
        for move in s:
            dx, dy = delta[move]
            x += dx
            y += dy
            prefix.append((x, y))
        total_x, total_y = prefix[-1]
        endpoints = set()
        for left in range(len(s) - k + 1):
            removed_x = prefix[left + k][0] - prefix[left][0]
            removed_y = prefix[left + k][1] - prefix[left][1]
            endpoints.add((total_x - removed_x, total_y - removed_y))
        return len(endpoints)
