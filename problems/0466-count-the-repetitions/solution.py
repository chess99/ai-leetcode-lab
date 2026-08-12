# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2) <= set(s1):
            return 0
        index2 = matched = blocks = 0
        seen = {}
        while blocks < n1:
            for char in s1:
                if char == s2[index2]:
                    index2 += 1
                    if index2 == len(s2):
                        index2 = 0
                        matched += 1
            blocks += 1
            if index2 in seen:
                previous_blocks, previous_matched = seen[index2]
                cycle_blocks = blocks - previous_blocks
                cycles = (n1 - blocks) // cycle_blocks
                matched += cycles * (matched - previous_matched)
                blocks += cycles * cycle_blocks
            else:
                seen[index2] = (blocks, matched)
        return matched // n2
