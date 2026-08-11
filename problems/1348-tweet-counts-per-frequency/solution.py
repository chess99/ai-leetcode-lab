from collections import defaultdict
from bisect import insort
class TweetCounts:
 def __init__(self):self.d=defaultdict(list)
 def recordTweet(self,n,t):insort(self.d[n],t)
 def getTweetCountsPerFrequency(self,f,n,startTime,endTime):
  step={'minute':60,'hour':3600,'day':86400}[f];return [sum(a<=x<=min(endTime,a+step-1) for x in self.d[n]) for a in range(startTime,endTime+1,step)]
