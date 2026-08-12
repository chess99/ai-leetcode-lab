# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = 1 + dp[i + 1][j + 1] if str1[i] == str2[j] else max(dp[i + 1][j], dp[i][j + 1])
        i = j = 0; answer = []
        while i < m and j < n:
            if str1[i] == str2[j]: answer.append(str1[i]); i += 1; j += 1
            elif dp[i + 1][j] >= dp[i][j + 1]: answer.append(str1[i]); i += 1
            else: answer.append(str2[j]); j += 1
        return "".join(answer) + str1[i:] + str2[j:]
