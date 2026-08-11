# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        first=binary.find('0')
        if first<0:return binary
        zeros=binary.count('0')
        return '1'* (first+zeros-1)+'0'+'1'*(len(binary)-first-zeros)
