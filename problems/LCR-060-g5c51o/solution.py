# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
 def topKFrequent(self,nums,k):return [x for x,_ in Counter(nums).most_common(k)]
