# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:50Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        quinorath = (s, target)
        prefix = []
        for i, char in enumerate(target):
            if count[char] == 0: break
            prefix.append(char); count[char] -= 1
        else:
            i = len(target)
        for pos in range(i, -1, -1):
            if pos < i:
                restored = target[pos]
                count[restored] += 1
                prefix.pop()
            for code in range(ord(target[pos]) + 1 if pos < len(target) else 123, 123):
                char = chr(code)
                if count[char]:
                    count[char] -= 1
                    suffix = ''.join(c * count[c] for c in sorted(count))
                    return ''.join(prefix) + char + suffix
        return ''
