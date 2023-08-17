class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if  not (dict.get(i)):
                dict[i]=1
            else:
                dict[i]+=1
        
        for i in dict.values():
            if(i>=2):
                return True
        return False
            