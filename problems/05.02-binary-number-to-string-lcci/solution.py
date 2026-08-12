# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def printBin(self, num: float) -> str:
        answer = ['0', '.']
        while num and len(answer) < 32:
            num *= 2
            if num >= 1:
                answer.append('1')
                num -= 1
            else:
                answer.append('0')
        return ''.join(answer) if num == 0 else 'ERROR'
