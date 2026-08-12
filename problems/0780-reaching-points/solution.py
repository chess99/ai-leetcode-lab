# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty >= sy:
            return (ty - sy) % sx == 0
        if ty == sy and tx >= sx:
            return (tx - sx) % sy == 0
        return False
