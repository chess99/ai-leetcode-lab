# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        answer=0;length=1
        while length*(length-1)//2<n:
            answer += (n-length*(length-1)//2)%length==0
            length+=1
        return answer
