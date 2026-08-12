# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        nums=list(map(int,s[::2])); ops=s[1::2]; n=len(nums)
        correct=0; product=nums[0]
        for op,x in zip(ops,nums[1:]):
            if op=='*': product*=x
            else: correct+=product; product=x
        correct+=product
        dp=[[set() for _ in range(n)] for _ in range(n)]
        for i,x in enumerate(nums):dp[i][i].add(x)
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                for p in range(i,j):
                    for a in dp[i][p]:
                        for b in dp[p+1][j]:
                            x=a+b if ops[p]=='+' else a*b
                            if x<=1000:dp[i][j].add(x)
        possible=dp[0][-1]; return sum(5 if x==correct else 2 if x in possible else 0 for x in answers)
