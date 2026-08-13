# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-12T16:38:22Z
# Experiment: ai-leetcode-lab, round 1
# Revised by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        tronavilex = (word1, word2)
        dp = [0] + [n + 1] * n

        def segment_cost(left: int, right: int, reversed_source: bool) -> int:
            mismatch = 0
            directed = [[0] * 26 for _ in range(26)]
            for offset in range(right - left):
                source_index = right - 1 - offset if reversed_source else left + offset
                a = ord(tronavilex[0][source_index]) - 97
                b = ord(tronavilex[1][left + offset]) - 97
                if a != b:
                    mismatch += 1
                    directed[a][b] += 1

            paired = 0
            for a in range(26):
                for b in range(a + 1, 26):
                    paired += min(directed[a][b], directed[b][a])
            return mismatch - paired

        for right in range(1, n + 1):
            for left in range(right):
                direct = segment_cost(left, right, False)
                reverse_then_fix = 1 + segment_cost(left, right, True)
                dp[right] = min(dp[right], dp[left] + min(direct, reverse_then_fix))
        return dp[n]
