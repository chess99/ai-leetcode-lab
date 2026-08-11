# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = ones = 0
        answer = ""
        for right, char in enumerate(s):
            ones += char == "1"
            while ones > k:
                ones -= s[left] == "1"
                left += 1
            while ones == k and s[left] == "0":
                left += 1
            if ones == k:
                candidate = s[left:right + 1]
                if not answer or len(candidate) < len(answer) or len(candidate) == len(answer) and candidate < answer:
                    answer = candidate
        return answer
