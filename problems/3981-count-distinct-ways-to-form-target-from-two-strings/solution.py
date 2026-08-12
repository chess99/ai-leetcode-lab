# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        valmorinth = (word1, word2, target)
        mod = 1_000_000_007
        n, m = len(word1), len(word2)
        dp = [[[0] * 4 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for wanted in target:
            nxt = [[[0] * 4 for _ in range(m + 1)] for _ in range(n + 1)]
            for j in range(m + 1):
                running = [0] * 4
                for i in range(n + 1):
                    for mask in range(4):
                        running[mask] = (running[mask] + dp[i][j][mask]) % mod
                    if i < n and word1[i] == wanted:
                        for mask in range(4):
                            nxt[i + 1][j][mask | 1] = (
                                nxt[i + 1][j][mask | 1] + running[mask]) % mod
            for i in range(n + 1):
                running = [0] * 4
                for j in range(m + 1):
                    for mask in range(4):
                        running[mask] = (running[mask] + dp[i][j][mask]) % mod
                    if j < m and word2[j] == wanted:
                        for mask in range(4):
                            nxt[i][j + 1][mask | 2] = (
                                nxt[i][j + 1][mask | 2] + running[mask]) % mod
            dp = nxt
        return sum(dp[i][j][3] for i in range(n + 1)
                   for j in range(m + 1)) % mod
