# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        answer = -10**9
        for odd_char in '01234':
            for even_char in '01234':
                if odd_char == even_char:
                    continue
                odd_prefix = [0] * (n + 1)
                even_prefix = [0] * (n + 1)
                for i, char in enumerate(s, 1):
                    odd_prefix[i] = odd_prefix[i - 1] + (char == odd_char)
                    even_prefix[i] = even_prefix[i - 1] + (char == even_char)

                minimum = [[10**9] * 2 for _ in range(2)]
                add = 0
                for right in range(k, n + 1):
                    while (
                        add <= right - k
                        and even_prefix[add] <= even_prefix[right] - 2
                    ):
                        parity_a = odd_prefix[add] & 1
                        parity_b = even_prefix[add] & 1
                        minimum[parity_a][parity_b] = min(
                            minimum[parity_a][parity_b],
                            odd_prefix[add] - even_prefix[add],
                        )
                        add += 1
                    best = minimum[1 - (odd_prefix[right] & 1)][even_prefix[right] & 1]
                    if best < 10**9:
                        answer = max(
                            answer,
                            odd_prefix[right] - even_prefix[right] - best,
                        )
        return answer
