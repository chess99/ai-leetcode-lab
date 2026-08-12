# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first={c:s.index(c)for c in set(s)};last={c:s.rindex(c)for c in set(s)};ranges=[]
        for c,a in first.items():
            b=last[c];i=a;ok=True
            while i<=b:
                if first[s[i]]<a:ok=False;break
                b=max(b,last[s[i]]);i+=1
            if ok:ranges.append((a,b))
        ans=[];end=-1
        for a,b in sorted(ranges,key=lambda x:x[1]):
            if a>end:ans.append(s[a:b+1]);end=b
        return ans
