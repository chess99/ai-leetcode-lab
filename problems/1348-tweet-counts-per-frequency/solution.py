# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from bisect import bisect_left, bisect_right, insort


class TweetCounts:
    def __init__(self):
        self.times = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.times[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> list[int]:
        bucket_size = {'minute': 60, 'hour': 3600, 'day': 86400}[freq]
        recorded = self.times[tweetName]
        counts = []
        for start in range(startTime, endTime + 1, bucket_size):
            end = min(endTime, start + bucket_size - 1)
            counts.append(bisect_right(recorded, end) - bisect_left(recorded, start))
        return counts
