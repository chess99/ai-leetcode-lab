class CustomStack:
 def __init__(self,maxSize:int):self.a=[];self.inc=[];self.m=maxSize
 def push(self,x:int)->None:
  if len(self.a)<self.m:self.a.append(x);self.inc.append(0)
 def pop(self)->int:
  if not self.a:return -1
  pending=self.inc.pop();x=self.a.pop()+pending
  if self.inc:self.inc[-1]+=pending
  return x
 def increment(self,k:int,val:int)->None:
  if self.inc:self.inc[min(k,len(self.inc))-1]+=val
