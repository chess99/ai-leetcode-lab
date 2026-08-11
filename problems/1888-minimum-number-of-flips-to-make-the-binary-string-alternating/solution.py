# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minFlips(self, s: str) -> int:
        doubled=s+s;first=second=0;answer=len(s)
        for i,char in enumerate(doubled):
            first+=(char!=('0' if i%2==0 else '1'));second+=(char!=('1' if i%2==0 else '0'))
            if i>=len(s):first-=(doubled[i-len(s)]!=('0' if (i-len(s))%2==0 else '1'));second-=(doubled[i-len(s)]!=('1' if (i-len(s))%2==0 else '0'))
            if i>=len(s)-1:answer=min(answer,first,second)
        return answer
