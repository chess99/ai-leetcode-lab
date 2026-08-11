# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51
        for start, end in ranges:
            for value in range(start, end + 1):
                covered[value] = True
        return all(covered[value] for value in range(left, right + 1))
