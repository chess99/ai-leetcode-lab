# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=depth=0
        for i,char in enumerate(s):
            if char=='(': depth+=1
            else:
                depth-=1
                if s[i-1]=='(': score+=1<<depth
        return score
