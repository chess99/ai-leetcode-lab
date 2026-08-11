class ProductOfNumbers:
 def __init__(self):self.p=[1]
 def add(self,num:int):self.p=[1] if num==0 else self.p+[self.p[-1]*num]
 def getProduct(self,k:int)->int:return 0 if k>=len(self.p) else self.p[-1]//self.p[-k-1]
