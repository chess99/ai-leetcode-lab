# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxOperations(self, s: str) -> int:
        ones = operations = 0
        for index, char in enumerate(s):
            if char == '1':
                ones += 1
            elif index and s[index - 1] == '1':
                operations += ones
        return operations
