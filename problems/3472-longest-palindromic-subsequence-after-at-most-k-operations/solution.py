# AI solution attribution
# Original handoff: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Current client: Codex Desktop
# Current model: gpt-5.6-sol
# Current reasoning effort: medium
# Current profile: sol-medium
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        width = k + 1

        # prev1 stores intervals of length length - 1, while prev2 stores
        # intervals of length length - 2.  An answer never exceeds n <= 200,
        # so one byte per state is sufficient.
        prev2 = [bytearray(width) for _ in range(n + 1)]
        prev1 = [bytearray([1]) * width for _ in range(n)]

        for length in range(2, n + 1):
            current = []
            for left in range(n - length + 1):
                right = left + length - 1
                skip_left = prev1[left + 1]
                skip_right = prev1[left]
                inner = prev2[left + 1]

                difference = abs(ord(s[left]) - ord(s[right]))
                cost = min(difference, 26 - difference)
                values = bytearray(width)

                for budget in range(width):
                    best = max(skip_left[budget], skip_right[budget])
                    if budget >= cost:
                        best = max(best, inner[budget - cost] + 2)
                    values[budget] = best

                current.append(values)

            prev2, prev1 = prev1, current

        return prev1[0][k]
