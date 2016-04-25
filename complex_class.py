class newcomplex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def copy(self):
        return newcomplex(self.r,self.i)
    def double(self):
        self.r=2*self.r
        self.i=2*self.i
    def __mul__(self,x):

        if isinstance(x,newcomplex):
            ans=self.copy()
            ans.r=self.r*x.r-self.i*x.i
            ans.i=self.r*x.i+self.i*x.r
            return ans
        else:
            ans=self.copy()
            ans.r=self.r*x
            ans.i=self.i*x
        return ans

            


