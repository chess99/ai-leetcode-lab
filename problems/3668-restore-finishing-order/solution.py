# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_ids = set(friends)
        return [person for person in order if person in friend_ids]
