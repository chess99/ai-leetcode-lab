# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isValid(self, code: str) -> bool:
        def valid_name(name):
            return 1 <= len(name) <= 9 and all('A' <= char <= 'Z' for char in name)

        stack=[]; i=0
        while i<len(code):
            if code.startswith('<![CDATA[',i):
                if not stack: return False
                end=code.find(']]>',i+9)
                if end<0:return False
                i=end+3
            elif code.startswith('</',i):
                end=code.find('>',i)
                if end<0:return False
                name=code[i+2:end]
                if not valid_name(name) or not stack or stack.pop()!=name:return False
                i=end+1
                if not stack and i<len(code):return False
            elif code[i]=='<':
                end=code.find('>',i)
                if end<0:return False
                name=code[i+1:end]
                if not valid_name(name):return False
                stack.append(name);i=end+1
            else:
                if not stack:return False
                i+=1
        return not stack
