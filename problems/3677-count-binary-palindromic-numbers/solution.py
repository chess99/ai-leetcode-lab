# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:return 1
        bits=n.bit_length();ans=1
        for length in range(1,bits):ans+=1<<((length-1)//2)
        half=(bits+1)//2;prefix=n>>(bits-half)
        def make(x):
            s=bin(x)[2:];return int(s+s[-(bits//2)-1::-1],2) if bits%2 else int(s+s[::-1],2)
        # Build without string ambiguity.
        value=prefix;tail=prefix>>(1 if bits%2 else 0)
        candidate=(prefix<<(bits//2))
        for i in range(bits//2):candidate|=((tail>>i)&1)<<(bits//2-1-i)
        return ans+prefix-(1<<(half-1))+(candidate<=n)
