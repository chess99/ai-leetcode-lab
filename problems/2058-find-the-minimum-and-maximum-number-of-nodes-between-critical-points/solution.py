# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:19Z
# Experiment: ai-leetcode-lab, round 1

from __future__ import annotations

from typing import List, Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        previous = head
        current = head.next if head else None
        index = 1
        first_critical = -1
        previous_critical = -1
        minimum_distance = float("inf")
        while current and current.next:
            following = current.next
            if (current.val > previous.val and current.val > following.val) or (
                current.val < previous.val and current.val < following.val
            ):
                if first_critical == -1:
                    first_critical = index
                else:
                    minimum_distance = min(minimum_distance, index - previous_critical)
                previous_critical = index
            previous = current
            current = following
            index += 1
        if previous_critical == -1 or previous_critical == first_critical:
            return [-1, -1]
        return [minimum_distance, previous_critical - first_critical]
