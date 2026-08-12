# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:55Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm=a//gcd(a,b)*b;low,high=1,n*min(a,b)
        while low<high:
            middle=(low+high)//2
            if middle//a+middle//b-middle//lcm>=n:high=middle
            else:low=middle+1
        return low%1_000_000_007
