# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        brenolcavi = words

        def minimum_rotation(text):
            if not text:
                return ''
            doubled = text + text
            i, j, offset = 0, 1, 0
            while i < len(text) and j < len(text) and offset < len(text):
                a, b = doubled[i + offset], doubled[j + offset]
                if a == b:
                    offset += 1
                    continue
                if a > b:
                    i = i + offset + 1
                    if i == j:
                        i += 1
                else:
                    j = j + offset + 1
                    if i == j:
                        j += 1
                offset = 0
            start = min(i, j)
            return doubled[start:start + len(text)]

        signatures = set()
        for word in words:
            signatures.add((len(word), minimum_rotation(word[::2]),
                            minimum_rotation(word[1::2])))
        return len(signatures)
