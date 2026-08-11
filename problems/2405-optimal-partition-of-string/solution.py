# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1
        seen = set()

        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()
            seen.add(char)

        return partitions
