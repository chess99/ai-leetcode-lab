# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n=len(s);h=n//2;a=s[:h];b=s[h:][::-1]
        pre=[[0]*26]
        for c in a:
            x=pre[-1][:];x[ord(c)-97]+=1;pre.append(x)
        preb=[[0]*26]
        for c in b:
            x=preb[-1][:];x[ord(c)-97]+=1;preb.append(x)
        bad=[0]
        for x,y in zip(a,b):bad.append(bad[-1]+(x!=y))
        def cnt(p,l,r):return [p[r+1][i]-p[l][i] for i in range(26)]
        out=[]
        for l,r,qr,qd in queries:
            c=n-1-qd;d=n-1-qr
            overlap_left=max(l,c);overlap_right=min(r,d)
            covered_bad=(bad[r+1]-bad[l])+(bad[d+1]-bad[c])
            if overlap_left<=overlap_right:
                covered_bad-=bad[overlap_right+1]-bad[overlap_left]
            if bad[h]-covered_bad:out.append(False);continue
            ca=cnt(pre,l,r);cb=cnt(preb,c,d)
            # Positions covered by exactly one mutable interval need their fixed mirror.
            for i in range(26):
                need_a=cnt(preb,l,r)[i]-cnt(preb,overlap_left,overlap_right)[i] if overlap_left<=overlap_right else cnt(preb,l,r)[i]
                need_b=cnt(pre,c,d)[i]-cnt(pre,overlap_left,overlap_right)[i] if overlap_left<=overlap_right else cnt(pre,c,d)[i]
                ca[i]-=need_a;cb[i]-=need_b
            out.append(ca==cb and min(ca)>=0 and min(cb)>=0)
        return out
