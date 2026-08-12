# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n=len(s);z=s.count('0')
        if z==0:return 0
        # State is zero count.  One operation can flip x zeroes and k-x ones.
        from collections import deque
        q=deque([z]);dist={z:0}
        while q:
            cur=q.popleft()
            for x in range(max(0,k-(n-cur)),min(k,cur)+1):
                nxt=cur+k-2*x
                if nxt==0:return dist[cur]+1
                if nxt not in dist:dist[nxt]=dist[cur]+1;q.append(nxt)
        return -1
