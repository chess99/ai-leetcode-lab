# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(","):
            slots -= 1
            if slots < 0:
                return False
            if node != "#":
                slots += 2
        return slots == 0
