# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char == '*':
                if result: result.pop()
            elif char == '#': result += result
            elif char == '%': result.reverse()
            else: result.append(char)
        return ''.join(result)
