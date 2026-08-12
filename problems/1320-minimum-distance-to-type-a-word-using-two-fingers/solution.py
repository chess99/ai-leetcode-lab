# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(a,b):return 0 if a==26 or b==26 else abs(a//6-b//6)+abs(a%6-b%6)
        dp={(26,26):0}
        for char in word:
            target=ord(char)-65;following={}
            for first,second in dp:
                cost=dp[first,second]
                following[target,second]=min(following.get((target,second),10**9),cost+distance(first,target))
                following[first,target]=min(following.get((first,target),10**9),cost+distance(second,target))
            dp=following
        return min(dp.values())
