# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n=len(text);seen=set()
        for length in range(1,n//2+1):
            for start in range(n-2*length+1):
                if text[start:start+length]==text[start+length:start+2*length]:seen.add(text[start:start+length])
        return len(seen)
