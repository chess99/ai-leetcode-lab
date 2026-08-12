# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumBoxes(self, n: int) -> int:
        layer=base=total=0
        while total+(layer+1)*(layer+2)//2<=n:layer+=1;total+=layer*(layer+1)//2;base+=layer
        extra=0
        while total<n:extra+=1;total+=extra
        return base+extra
