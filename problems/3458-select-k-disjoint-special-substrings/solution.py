# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k==0:return True
        first={c:s.index(c) for c in set(s)}; last={c:s.rindex(c) for c in set(s)}; intervals=[]
        for c,left in first.items():
            right=last[c]; i=left; valid=True
            while i<=right:
                if first[s[i]]<left: valid=False; break
                right=max(right,last[s[i]]); i+=1
            if valid and not (left==0 and right==len(s)-1): intervals.append((right,left))
        intervals.sort(); count=0; end=-1
        for right,left in intervals:
            if left>end: count+=1; end=right
        return count>=k
