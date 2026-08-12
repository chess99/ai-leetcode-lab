# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter, deque
        chars=[c for c,v in Counter(s).items() if v>=k]
        ans=''
        def ok(t):
            i=rep=0
            for c in s:
                if c==t[i]:
                    i+=1
                    if i==len(t):
                        rep+=1;i=0
                        if rep==k:return True
            return False
        q=deque([''])
        while q:
            cur=q.popleft()
            for c in chars:
                nxt=cur+c
                if ok(nxt):
                    if len(nxt)>len(ans) or len(nxt)==len(ans) and nxt>ans:ans=nxt
                    q.append(nxt)
        return ans
