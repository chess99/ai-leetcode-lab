# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findIntegers(self, n: int) -> int:
        dp=[1,2]
        for _ in range(2,32):dp.append(dp[-1]+dp[-2])
        answer=0; previous=0
        for bit in range(30,-1,-1):
            if n&(1<<bit):
                answer+=dp[bit]
                if previous:return answer
                previous=1
            else:previous=0
        return answer+1
