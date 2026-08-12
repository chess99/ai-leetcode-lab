# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        pieces = []
        balance = start = 0
        for index, char in enumerate(s):
            balance += 1 if char == '1' else -1
            if balance == 0:
                pieces.append('1' + self.makeLargestSpecial(s[start + 1:index]) + '0')
                start = index + 1
        return ''.join(sorted(pieces, reverse=True))
