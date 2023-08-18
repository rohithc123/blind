class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = list()
        for i in strs:
            k = dict()
            for x in i:
                k[x]=1+k.get(x,0)
            temp.append(k)
        ans = list()

        check = [1]*(len(temp))

        for i in range(0,len(temp)):
            if(not check[i]):
                continue
            
            check[i]=0
            k = list()
            k.append(strs[i])
            
            for j in range(i+1,len(temp)):
                if temp[i]==temp[j] and check[j]:
                    k.append(strs[j])
                    check[j]=0
        
                
            ans.append(k)
        
        return ans