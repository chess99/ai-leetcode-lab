# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def processStr(self, s: str, k: int) -> str:
        cap = 10**15 + 1
        lengths = []
        length = 0
        for ch in s:
            if 'a' <= ch <= 'z': length += 1
            elif ch == '*': length = max(0, length - 1)
            elif ch == '#': length = min(cap, length * 2)
            lengths.append(length)
        if k < 0 or k >= length:
            return '.'
        reverse = False
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]; before = lengths[i - 1] if i else 0; after = lengths[i]
            if ch == '#':
                if k >= before: k -= before
            elif ch == '%':
                k = before - 1 - k; reverse = not reverse
            elif ch == '*':
                # The deleted last position cannot be queried in this prefix.
                pass
            elif k == before:
                return ch
        return '.'
