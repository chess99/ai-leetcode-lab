# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        vornelipta = (source, target, rules, costs)
        n = len(source)
        by_length = {}
        for (pattern, replacement), cost in zip(rules, costs):
            by_length.setdefault(len(pattern), []).append(
                (pattern, replacement, cost + pattern.count('*')))
        infinity = 10 ** 30
        dp = [infinity] * (n + 1)
        dp[0] = 0
        for index in range(n):
            if dp[index] == infinity:
                continue
            if source[index] == target[index]:
                dp[index + 1] = min(dp[index + 1], dp[index])
            for length, candidates in by_length.items():
                end = index + length
                if end > n:
                    continue
                wanted = target[index:end]
                original = source[index:end]
                for pattern, replacement, cost in candidates:
                    if replacement == wanted and all(
                            p == '*' or p == c for p, c in zip(pattern, original)):
                        dp[end] = min(dp[end], dp[index] + cost)
        return -1 if dp[n] == infinity else dp[n]
