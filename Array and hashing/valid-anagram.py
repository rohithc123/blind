class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        a = dict()
        b = dict()

        for i in range (0,len(s)):

            a[s[i]]=1+ a.get(s[i],0);
            b[t[i]]=1+ b.get(t[i],0);
        
        return a==b

        
        # my first implementation
        # for x in s:
        #     if not (x in a):
        #         a[x]=1
        #     else:
        #         a[x]+=1
        
        # for x in t:
        #     if not (x in b):
        #         b[x]=1
        #     else:
        #         b[x]+=1

        # for x in a.keys():
        #     if not (x in b):
        #         return False
        #     elif a[x] != b[x]:
        #         return False

        
        # for x in b.keys():
        #     if not (x in a):
        #         return False
        #     elif a[x] != b[x]:
        #         return False

        # return True 
