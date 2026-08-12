# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod=10**9+7
        def f(s):
            from functools import lru_cache
            @lru_cache(None)
            def dp(i,sm,tight):
                if sm>max_sum:return 0
                if i==len(s):return min_sum<=sm<=max_sum
                return sum(dp(i+1,sm+d,tight and d==int(s[i]))for d in range((int(s[i])if tight else 9)+1))%mod
            return dp(0,0,True)
        return (f(num2)-f(str(int(num1)-1)))%mod
