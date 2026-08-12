# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:08:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def clumsy(self, n: int) -> int:
        stack=[n]; n-=1; operation=0
        while n:
            if operation==0: stack[-1]=stack[-1]*n
            elif operation==1:
                value = stack[-1]
                stack[-1] = abs(value) // n * (1 if value >= 0 else -1)
            elif operation==2: stack.append(n)
            else: stack.append(-n)
            n-=1;operation=(operation+1)%4
        return sum(stack)
