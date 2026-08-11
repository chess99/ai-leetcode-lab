# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1_000_000_007
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        for _ in range(t):
            nxt = [0] * 26
            for i in range(25):
                nxt[i + 1] = count[i]
            nxt[0] = count[25]
            nxt[1] = (nxt[1] + count[25]) % mod
            count = nxt
        return sum(count) % mod
