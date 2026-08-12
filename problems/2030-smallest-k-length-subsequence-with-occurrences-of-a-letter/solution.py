# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        remain=s.count(letter); need=repetition; st=[]
        for i,c in enumerate(s):
            while st and st[-1]>c and len(st)-1+len(s)-i>=k and (st[-1]!=letter or remain>need):
                if st.pop()==letter:need+=1
            if len(st)<k and (c==letter or k-len(st)>need):
                st.append(c)
                if c==letter:need-=1
            if c==letter:remain-=1
        return ''.join(st)
