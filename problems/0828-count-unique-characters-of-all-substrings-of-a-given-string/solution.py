# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        positions={};answer=0
        for index,char in enumerate(s):
            previous,second=positions.get(char,(-1,-1))
            answer+=(index-previous)*(previous-second)
            positions[char]=(index,previous)
        n=len(s)
        for previous,second in positions.values():answer+=(n-previous)*(previous-second)
        return answer
