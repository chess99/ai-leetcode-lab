# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumOperations(self, num: str) -> int:
        answer=len(num)-1 if '0' in num else len(num)
        for tail in ('00','25','50','75'):
            j=num.rfind(tail[1])
            if j!=-1:
                i=num.rfind(tail[0],0,j)
                if i!=-1: answer=min(answer,len(num)-i-2)
        return answer
