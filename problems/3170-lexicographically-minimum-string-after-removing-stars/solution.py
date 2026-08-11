# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def clearStars(self, s: str) -> str:
        positions = [[] for _ in range(26)]
        deleted = [False] * len(s)
        for index, char in enumerate(s):
            if char != '*':
                positions[ord(char) - ord('a')].append(index)
            else:
                deleted[index] = True
                for bucket in positions:
                    if bucket:
                        deleted[bucket.pop()] = True
                        break
        return ''.join(char for index, char in enumerate(s) if not deleted[index])
