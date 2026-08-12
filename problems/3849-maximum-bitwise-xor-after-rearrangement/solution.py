# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        selunaviro = (s, t)
        ones = t.count('1')
        zeros = len(t) - ones
        answer = []
        for char in s:
            if char == '0' and ones:
                answer.append('1'); ones -= 1
            elif char == '1' and zeros:
                answer.append('1'); zeros -= 1
            else:
                answer.append('0')
        return ''.join(answer)
