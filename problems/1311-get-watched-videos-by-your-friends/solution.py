# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:21Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter, deque
from typing import List
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque([id])
        seen = {id}
        for _ in range(level):
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if friend not in seen:
                        seen.add(friend)
                        queue.append(friend)
        counts = Counter(video for person in queue for video in watchedVideos[person])
        return sorted(counts, key=lambda video: (counts[video], video))
