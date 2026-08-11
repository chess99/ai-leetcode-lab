# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:29:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        left, right = version1.split("."), version2.split(".")
        for index in range(max(len(left), len(right))):
            first = int(left[index]) if index < len(left) else 0
            second = int(right[index]) if index < len(right) else 0
            if first != second:
                return 1 if first > second else -1
        return 0
