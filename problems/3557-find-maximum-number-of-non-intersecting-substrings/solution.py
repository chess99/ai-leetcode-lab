# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSubstrings(self, word: str) -> int:
        # 对每个右端点，最短的同字母合法区间总是最优。
        eligible = [-10**9] * 26
        answer = 0
        end = -1
        for i, ch in enumerate(word):
            if i >= 3:
                eligible[ord(word[i - 3]) - 97] = i - 3
            p = eligible[ord(ch) - 97]
            if i - p >= 3 and p > end:
                answer += 1
                end = i
        return answer
