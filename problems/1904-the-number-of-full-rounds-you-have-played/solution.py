# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def minutes(time):
            hour,minute=map(int,time.split(':'));return 60*hour+minute
        start,end=minutes(loginTime),minutes(logoutTime)
        if end<start:end+=1440
        start=(start+14)//15*15;end=end//15*15
        return max(0,(end-start)//15)
