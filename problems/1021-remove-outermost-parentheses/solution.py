# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=[]; depth=0
        for char in s:
            if char=='(':
                if depth: result.append(char)
                depth+=1
            else:
                depth-=1
                if depth: result.append(char)
        return ''.join(result)
