# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        from fractions import Fraction
        def search(values):
            if len(values)==1:return values[0]==24
            for i in range(len(values)):
                for j in range(i):
                    rest=[values[x]for x in range(len(values))if x not in (i,j)];a,b=values[i],values[j]
                    for value in (a+b,a-b,b-a,a*b,*(() if not b else (a/b,)),*(() if not a else (b/a,))):
                        if search(rest+[value]):return True
            return False
        return search(list(map(Fraction,cards)))
