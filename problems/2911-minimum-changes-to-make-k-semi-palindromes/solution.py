# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        size = len(s)
        cost = [[10 ** 9] * size for _ in range(size)]
        for left in range(size):
            for right in range(left + 1, size):
                length = right - left + 1
                divisor = 1
                while divisor < length:
                    if length % divisor == 0:
                        changes = 0
                        group_length = length // divisor
                        for offset in range(divisor):
                            for index in range(group_length // 2):
                                changes += (
                                    s[left + offset + index * divisor]
                                    != s[left + offset + (group_length - 1 - index) * divisor]
                                )
                        cost[left][right] = min(cost[left][right], changes)
                    divisor += 1
        infinity = 10 ** 9
        dynamic = [[infinity] * (size + 1) for _ in range(k + 1)]
        dynamic[0][0] = 0
        for groups in range(1, k + 1):
            for end in range(2 * groups, size + 1):
                for start in range(2 * (groups - 1), end - 1):
                    dynamic[groups][end] = min(
                        dynamic[groups][end],
                        dynamic[groups - 1][start] + cost[start][end - 1],
                    )
        return dynamic[k][size]
