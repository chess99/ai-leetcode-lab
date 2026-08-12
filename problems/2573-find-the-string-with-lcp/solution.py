# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        size = len(lcp)
        characters = [""] * size
        current = 0
        for index in range(size):
            if characters[index]:
                continue
            if current == 26:
                return ""
            character = chr(97 + current)
            current += 1
            for other in range(index, size):
                if lcp[index][other] > 0:
                    characters[other] = character

        for first in range(size - 1, -1, -1):
            for second in range(size - 1, -1, -1):
                expected = 0
                if characters[first] == characters[second]:
                    expected = 1
                    if first + 1 < size and second + 1 < size:
                        expected += lcp[first + 1][second + 1]
                if lcp[first][second] != expected:
                    return ""
        return "".join(characters)
