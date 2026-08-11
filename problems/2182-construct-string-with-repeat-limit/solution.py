# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        answer = []
        high = 25
        while high >= 0:
            while high >= 0 and counts[chr(ord('a') + high)] == 0:
                high -= 1
            if high < 0:
                break
            letter = chr(ord('a') + high)
            used = min(counts[letter], repeatLimit)
            answer.append(letter * used)
            counts[letter] -= used
            if counts[letter] == 0:
                continue
            lower = high - 1
            while lower >= 0 and counts[chr(ord('a') + lower)] == 0:
                lower -= 1
            if lower < 0:
                break
            separator = chr(ord('a') + lower)
            answer.append(separator)
            counts[separator] -= 1
        return ''.join(answer)
