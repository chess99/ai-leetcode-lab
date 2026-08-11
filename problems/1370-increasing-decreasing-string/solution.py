# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:52:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        counts, result = Counter(s), []
        while len(result) < len(s):
            for ch in sorted(counts):
                if counts[ch]: result.append(ch); counts[ch] -= 1
            for ch in sorted(counts, reverse=True):
                if counts[ch]: result.append(ch); counts[ch] -= 1
        return ''.join(result)
