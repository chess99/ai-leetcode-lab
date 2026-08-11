# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:13:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions=((0,1),(1,0),(0,-1),(-1,0));x=y=direction=0
        for instruction in instructions:
            if instruction=='G': dx,dy=directions[direction];x+=dx;y+=dy
            elif instruction=='L':direction=(direction-1)%4
            else:direction=(direction+1)%4
        return (x,y)==(0,0) or direction!=0
