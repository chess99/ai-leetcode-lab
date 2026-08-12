# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t); missing = len(t); left = start = 0; best = len(s) + 1
        for right, ch in enumerate(s, 1):
            if need[ch] > 0: missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left < best: start, best = left, right - left
                ch = s[left]; need[ch] += 1; left += 1
                if need[ch] > 0: missing += 1
        return '' if best > len(s) else s[start:start+best]
