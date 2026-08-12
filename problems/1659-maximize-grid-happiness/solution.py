# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        from functools import lru_cache
        states=3**n;digits=[];intro=[];extro=[];inside=[]
        interaction=((0,0,0),(0,-60,-10),(0,-10,40))
        for state in range(states):
            row=[];value=state
            for _ in range(n):row.append(value%3);value//=3
            digits.append(row);intro.append(row.count(1));extro.append(row.count(2));score=0
            for i,x in enumerate(row):
                if x:score+=120 if x==1 else 40
                if i and x and row[i-1]:score+=interaction[x][row[i-1]]
            inside.append(score)
        between=[[sum(interaction[a][b] for a,b in zip(digits[x],digits[y]) if a and b) for y in range(states)] for x in range(states)]
        @lru_cache(None)
        def dp(row,previous,left_i,left_e):
            if row==m:return 0
            best=0
            for state in range(states):
                if intro[state]<=left_i and extro[state]<=left_e:best=max(best,inside[state]+between[previous][state]+dp(row+1,state,left_i-intro[state],left_e-extro[state]))
            return best
        return dp(0,0,introvertsCount,extrovertsCount)
