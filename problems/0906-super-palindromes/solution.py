# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        low,high=int(left),int(right);answer=0
        for root in range(1,100000):
            s=str(root)
            for p in (int(s+s[-2::-1]),int(s+s[::-1])):
                square=p*p
                if low<=square<=high and str(square)==str(square)[::-1]:answer+=1
        return answer
