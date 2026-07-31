class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for word in strs:
            length = len(word)
            symbol = str(length)+ "$"
            enc_str += symbol + word
        return enc_str


    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i < len(s):
            num_str = ""
            str1=""
            while s[i]!= "$":
                num_str += s[i]
                i+=1
            num = int(num_str)
            i+=1
            for k in range(i,i+num):
                str1+=s[k]
            i+=num
            
            res.append(str1)
        return res
            

        
       
