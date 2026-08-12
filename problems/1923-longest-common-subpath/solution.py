# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        paths.sort(key=len);mod1,mod2=1_000_000_007,1_000_000_009;base=1_000_003
        def hashes(path,length):
            if length==0:return {(0,0)}
            p1=pow(base,length,mod1);p2=pow(base,length,mod2);h1=h2=0;result=set()
            for i,value in enumerate(path):
                value+=1;h1=(h1*base+value)%mod1;h2=(h2*base+value)%mod2
                if i>=length:h1=(h1-(path[i-length]+1)*p1)%mod1;h2=(h2-(path[i-length]+1)*p2)%mod2
                if i+1>=length:result.add((h1,h2))
            return result
        def possible(length):
            common=hashes(paths[0],length)
            for path in paths[1:]:
                common&=hashes(path,length)
                if not common:return False
            return True
        low,high=0,len(paths[0])
        while low<high:
            middle=(low+high+1)//2
            if possible(middle):low=middle
            else:high=middle-1
        return low
