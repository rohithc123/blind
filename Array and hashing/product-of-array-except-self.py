class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = int(1)
        temp = collections.defaultdict()

        for i in nums:
            ans=ans*i
            temp[i]=1+temp.get(i,0)
        
        if temp.get(0,0)>1:
            res = []
            for i in range(0,len(nums)):
                res.append(0)
            return res
        
        else:
            res = []
            for i in nums:
                if i!=0:
                    res.append(int(ans/i))
                else:
                    y=1
                    for i in nums:
                        if i!=0:
                            y=y*i
                    res.append(y)
            return res
                
                