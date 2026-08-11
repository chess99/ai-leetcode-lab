# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:19Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from typing import List


class Solution:
    def mostPopularCreator(
        self, creators: List[str], ids: List[str], views: List[int]
    ) -> List[List[str]]:
        total = defaultdict(int)
        best_video = {}

        for creator, video_id, view_count in zip(creators, ids, views):
            total[creator] += view_count
            if (
                creator not in best_video
                or view_count > best_video[creator][0]
                or (
                    view_count == best_video[creator][0]
                    and video_id < best_video[creator][1]
                )
            ):
                best_video[creator] = (view_count, video_id)

        highest_total = max(total.values())
        return [
            [creator, best_video[creator][1]]
            for creator, popularity in total.items()
            if popularity == highest_total
        ]
