# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        if len(first) > len(second):
            first, second = second, first
        left = right = differences = 0
        while left < len(first) and right < len(second):
            if first[left] == second[right]:
                left += 1
                right += 1
                continue
            differences += 1
            if differences > 1:
                return False
            if len(first) == len(second):
                left += 1
            right += 1
        return True
