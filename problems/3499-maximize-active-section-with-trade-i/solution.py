# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        runs = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j
        best_gain = 0
        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1' and runs[i - 1][0] == runs[i + 1][0] == '0':
                best_gain = max(best_gain, runs[i - 1][1] + runs[i + 1][1])
        return s.count('1') + best_gain
