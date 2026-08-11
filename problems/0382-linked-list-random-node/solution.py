# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:42Z
# Experiment: ai-leetcode-lab, round 1
import random
from typing import Optional


class Solution:
    def __init__(self, head: Optional["ListNode"]):
        self.head = head

    def getRandom(self) -> int:
        chosen = self.head.val
        node = self.head.next
        count = 2
        while node:
            if random.randrange(count) == 0:
                chosen = node.val
            node = node.next
            count += 1
        return chosen
