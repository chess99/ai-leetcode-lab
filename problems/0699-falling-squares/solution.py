# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals=[];answer=[];best=0
        for left,size in positions:
            right=left+size;height=size
            for start,end,top in intervals:
                if left<end and start<right:height=max(height,top+size)
            intervals.append((left,right,height));best=max(best,height);answer.append(best)
        return answer
