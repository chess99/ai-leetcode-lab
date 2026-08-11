# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:01:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        fixed = [False] * (len(strs) - 1)
        deletions = 0
        for column in range(len(strs[0])):
            if any(not fixed[row] and strs[row][column] > strs[row + 1][column]
                   for row in range(len(fixed))):
                deletions += 1
                continue
            for row in range(len(fixed)):
                if strs[row][column] < strs[row + 1][column]:
                    fixed[row] = True
        return deletions
