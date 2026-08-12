# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s: str) -> int:
        trinovalex = s
        # 最大字母可以逐级与更小字母合并，最终一起走到 z 再变为 a。
        return 0 if set(trinovalex) == {'a'} else ord('z') - min(map(ord, (ch for ch in trinovalex if ch != 'a'))) + 1
