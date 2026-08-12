# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        req=[]
        for p in (2,3,5,7):
            c=0
            while t%p==0:t//=p;c+=1
            req.append(c)
        if t>1:return '-1'
        fac={str(d):v for d,v in [(1,(0,0,0,0)),(2,(1,0,0,0)),(3,(0,1,0,0)),(4,(2,0,0,0)),(5,(0,0,1,0)),(6,(1,1,0,0)),(7,(0,0,0,1)),(8,(3,0,0,0)),(9,(0,2,0,0))]}
        def need(a):
            from functools import lru_cache
            @lru_cache(None)
            def build(state):
                if not any(state):return ''
                best=None
                for d in range(2,10):
                    nxt=tuple(max(0,state[j]-fac[str(d)][j]) for j in range(4))
                    if nxt==state:continue
                    candidate=''.join(sorted(str(d)+build(nxt)))
                    if best is None or (len(candidate),candidate)<(len(best),best):best=candidate
                return best
            return build(tuple(a))
        pref=[req[:]]
        for c in num:
            a=pref[-1][:]
            if c!='0':
                for j,v in enumerate(fac[c]):a[j]=max(0,a[j]-v)
            pref.append(a)
        if '0' not in num and not any(pref[-1]):return num
        n=len(num)
        first_zero=num.find('0')
        stop=n-1 if first_zero<0 else first_zero
        for i in range(stop,-1,-1):
            for d in range(int(num[i])+1,10):
                a=pref[i][:]
                for j,v in enumerate(fac[str(d)]):a[j]=max(0,a[j]-v)
                tail=need(a)
                if len(tail)<=n-i-1:return num[:i]+str(d)+'1'*(n-i-1-len(tail))+tail
        tail=need(req)
        return '1'*(max(n+1,len(tail))-len(tail))+tail
