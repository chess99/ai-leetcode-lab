# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:54:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        compressed = []
        count = 1
        for index in range(1, len(S) + 1):
            if index < len(S) and S[index] == S[index - 1]:
                count += 1
            else:
                compressed.append(S[index - 1] + str(count))
                count = 1
        result = ''.join(compressed)
        return result if len(result) < len(S) else S
