# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace('X', '') != result.replace('X', ''): return False
        start_positions = [(char, i) for i, char in enumerate(start) if char != 'X']
        result_positions = [(char, i) for i, char in enumerate(result) if char != 'X']
        return all((char != 'L' or old >= new) and (char != 'R' or old <= new) for (char, old), (_, new) in zip(start_positions, result_positions))
