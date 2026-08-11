# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:59Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Twitter:

    def __init__(self):
        self.time = 0; self.tweets = defaultdict(list); self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId)); self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        return [tweet for _, tweet in sorted((item for user in users for item in self.tweets[user]), reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
