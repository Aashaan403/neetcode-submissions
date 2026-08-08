class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r =0
        count = {}# for storing each charcter and its max count in the window
        maxim = 0
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0

        while r < len(s) :
            count[s[r]] = count.get(s[r],0) + 1
            if  ((r-l+1) - max(count.values()) <= k ) : #checks whether the maximumum element in the 
                maxim = max(maxim,r-l+1)
               
            else:
                count[s[l]] -= 1
                l += 1
            
            r+=1

            
                    
        return maxim
        
        


            
        
        

                

            

            
            
        
        