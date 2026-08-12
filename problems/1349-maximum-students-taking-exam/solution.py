# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        columns=len(seats[0]);dp={0:0}
        for row in seats:
            available=sum((char=='.')<<i for i,char in enumerate(row));following={}
            for mask in range(1<<columns):
                if mask&~available or mask&(mask<<1):continue
                for previous,score in dp.items():
                    if mask&(previous<<1) or mask&(previous>>1):continue
                    following[mask]=max(following.get(mask,0),score+mask.bit_count())
            dp=following
        return max(dp.values())
