# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        balance = [0] * 26
        for char in p:
            balance[ord(char) - 97] += 1
        missing = len(p)
        answer = []
        for index, char in enumerate(s):
            value = ord(char) - 97
            if balance[value] > 0:
                missing -= 1
            balance[value] -= 1
            if index >= len(p):
                old = ord(s[index - len(p)]) - 97
                balance[old] += 1
                if balance[old] > 0:
                    missing += 1
            if missing == 0:
                answer.append(index - len(p) + 1)
        return answer
