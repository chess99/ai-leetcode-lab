# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDecodings(self, s: str) -> int:
        mod=10**9+7
        def one(c):return 9 if c=='*' else int(c!='0')
        def two(a,b):
            if a=='*' and b=='*':return 15
            if a=='*':return 2 if b<='6' else 1
            if b=='*':return 9 if a=='1' else 6 if a=='2' else 0
            return int(10<=int(a+b)<=26)
        if not s:
            return 0
        prev,cur=1,one(s[0])
        for i in range(1,len(s)):prev,cur=cur,(cur*one(s[i])+prev*two(s[i-1],s[i]))%mod
        return cur
