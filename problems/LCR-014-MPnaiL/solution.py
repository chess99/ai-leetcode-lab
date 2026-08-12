# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        balance = [0] * 26
        for char in s1:
            balance[ord(char) - 97] += 1
        missing = len(s1)
        for index, char in enumerate(s2):
            value = ord(char) - 97
            if balance[value] > 0:
                missing -= 1
            balance[value] -= 1
            if index >= len(s1):
                old = ord(s2[index - len(s1)]) - 97
                balance[old] += 1
                if balance[old] > 0:
                    missing += 1
            if missing == 0:
                return True
        return False
