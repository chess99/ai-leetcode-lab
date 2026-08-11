# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups={}
        for value in range(1,n+1):
            digit_sum=sum(map(int,str(value))); groups[digit_sum]=groups.get(digit_sum,0)+1
        maximum=max(groups.values()); return sum(count==maximum for count in groups.values())
