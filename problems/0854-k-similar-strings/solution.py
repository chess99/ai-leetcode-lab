# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:54Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue=deque([(s1,0)]);seen={s1}
        while queue:
            word,steps=queue.popleft()
            if word==s2:return steps
            index=next(i for i,(a,b) in enumerate(zip(word,s2)) if a!=b)
            chars=list(word)
            for following in range(index+1,len(word)):
                if chars[following]==s2[index] and chars[following]!=s2[following]:
                    chars[index],chars[following]=chars[following],chars[index];candidate=''.join(chars);chars[index],chars[following]=chars[following],chars[index]
                    if candidate not in seen:seen.add(candidate);queue.append((candidate,steps+1))
