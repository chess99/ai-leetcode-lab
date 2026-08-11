# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        owners = {}
        for index, word in enumerate(arr):
            for start in range(len(word)):
                for end in range(start + 1, len(word) + 1):
                    owners.setdefault(word[start:end], set()).add(index)
        answer = []
        for index, word in enumerate(arr):
            found = ""
            for length in range(1, len(word) + 1):
                choices = {word[start:start + length] for start in range(len(word) - length + 1) if owners[word[start:start + length]] == {index}}
                if choices:
                    found = min(choices)
                    break
            answer.append(found)
        return answer
