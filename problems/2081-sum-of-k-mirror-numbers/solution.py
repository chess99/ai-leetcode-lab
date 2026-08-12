# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def pal(x):
            s=str(x);return int(s+s[-2::-1])
        def basepal(x):
            a=[]
            while x:a.append(x%k);x//=k
            return a==a[::-1]
        ans=got=0; length=1
        while got<n:
            for half in range(10**((length-1)//2),10**((length+1)//2)):
                x=pal(half) if length%2 else int(str(half)+str(half)[::-1])
                if basepal(x):ans+=x;got+=1
                if got==n:return ans
            length+=1
