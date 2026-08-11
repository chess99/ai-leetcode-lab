# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:21Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 1_000_000_007
        n = len(pressedKeys)
        ways3 = [0] * (n + 1)
        ways4 = [0] * (n + 1)
        ways3[0] = ways4[0] = 1

        for length in range(1, n + 1):
            ways3[length] = sum(ways3[max(0, length - 3):length]) % mod
            ways4[length] = sum(ways4[max(0, length - 4):length]) % mod

        answer = 1
        start = 0
        while start < n:
            end = start
            while end < n and pressedKeys[end] == pressedKeys[start]:
                end += 1
            length = end - start
            answer = answer * (ways4[length] if pressedKeys[start] in "79" else ways3[length]) % mod
            start = end

        return answer
