class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  
        #store the count of each elements in the count hash map yeah?
        count1 = {}
        for i in range(len(s1)):
            if s1[i] not in count1:
                count1[s1[i]] = 1
            else:
                count1[s1[i]] += 1


        count2 = {}
        #ഇനി ഒരു വിൻഡോ വേണം.
        l = 0
        r = len(s1)-1
        for k in range(l,len(s1)):
            if s2[k] not in count2:
                count2[s2[k]] = 1
            else:
                count2[s2[k]] += 1

        
        while r < len(s2):
            if count1 == count2:
                return True 
            
            if r+1 < len(s2):
                if s2[r+1] not in count2:
                    count2[s2[r+1]] = 1
                else:
                    count2[s2[r+1]] +=1 
            r+=1    
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]] 
            l+=1
        
        if count1 == count2:

            return True 
        else:
            return False
        
       

               
            
            
            
        
            

            

        
            
        