# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod=1_000_000_007;m=r-l+1
        if n==1:return m
        # State is (last value, direction); transition matrices are constant.
        size=2*m
        mat=[[0]*size for _ in range(size)]
        for x in range(m):
            for y in range(m):
                if y>x:mat[y][x+m]=1
                if y<x:mat[y+m][x]=1
        def mul(a,b):
            c=[[0]*size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if a[i][k]:
                        for j in range(size):c[i][j]=(c[i][j]+a[i][k]*b[k][j])%mod
            return c
        vec=[1]*size;power=mat;exp=n-1
        while exp:
            if exp&1:
                vec=[sum(power[i][j]*vec[j] for j in range(size))%mod for i in range(size)]
            power=mul(power,power);exp//=2
        return sum(vec)%mod
