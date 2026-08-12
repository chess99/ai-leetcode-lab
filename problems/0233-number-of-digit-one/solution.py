# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countDigitOne(self, n: int) -> int:
        answer = 0; place = 1
        while place <= n:
            high, current, low = n // (place * 10), (n // place) % 10, n % place
            if current == 0: answer += high * place
            elif current == 1: answer += high * place + low + 1
            else: answer += (high + 1) * place
            place *= 10
        return answer
