# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a=list(s);n=len(a)
        for i in range(n-1,-1,-1):
            for x in range(ord(a[i])+1,ord('a')+k):
                if (i<1 or chr(x)!=a[i-1]) and (i<2 or chr(x)!=a[i-2]):
                    a[i]=chr(x)
                    for j in range(i+1,n):
                        for y in range(ord('a'),ord('a')+k):
                            if (j<1 or chr(y)!=a[j-1]) and (j<2 or chr(y)!=a[j-2]):a[j]=chr(y);break
                    return ''.join(a)
        return ''
