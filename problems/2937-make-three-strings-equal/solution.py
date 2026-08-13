# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:19Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        common_length = 0
        for chars in zip(s1, s2, s3):
            if len(set(chars)) > 1:
                break
            common_length += 1

        if common_length == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * common_length
