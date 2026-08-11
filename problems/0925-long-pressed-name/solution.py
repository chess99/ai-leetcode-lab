# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        index = 0
        for char in typed:
            if index < len(name) and char == name[index]:
                index += 1
            elif index == 0 or char != name[index - 1]:
                return False
        return index == len(name)
