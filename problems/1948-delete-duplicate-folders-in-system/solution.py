# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:01Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root={}
        for path in paths:
            node=root
            for name in path:node=node.setdefault(name,{})
        signature_count=Counter();signature_by_node={};intern={};next_signature=1
        def identify(node):
            nonlocal next_signature
            if not node:return 0
            structure=tuple((name,identify(child)) for name,child in sorted(node.items()))
            if structure not in intern:intern[structure]=next_signature;next_signature+=1
            signature=intern[structure];signature_by_node[id(node)]=signature;signature_count[signature]+=1
            return signature
        identify(root);answer=[]
        def collect(node,path):
            for name,child in node.items():
                signature=signature_by_node.get(id(child),0)
                if signature and signature_count[signature]>1:continue
                answer.append(path+[name]);collect(child,path+[name])
        collect(root,[]);return answer
