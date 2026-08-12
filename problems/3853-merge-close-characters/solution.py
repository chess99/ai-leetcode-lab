# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        velunorati = s
        chars = list(s)
        while True:
            pair = None
            for left in range(len(chars)):
                for right in range(left + 1, min(len(chars), left + k + 1)):
                    if chars[left] == chars[right]:
                        pair = right
                        break
                if pair is not None:
                    break
            if pair is None:
                return ''.join(chars)
            chars.pop(pair)
