class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False 
           
        l = 0
        s1Counts = {}
        s2Counts = {}

        for i in range(len(s1)):
            s1Counts[s1[i]] = s1Counts.get(s1[i] , 0 ) + 1
            s2Counts[s2[i]] = s2Counts.get(s2[i] , 0) + 1

        if s1Counts == s2Counts: return True

        for r in range(len(s1) , len(s2)):

            r_char = s2[r]
            s2Counts[r_char] = s2Counts.get(r_char , 0) + 1


            l_char = s2[l]
            s2Counts[l_char] -= 1 

            if s2Counts[l_char] == 0:
                del s2Counts[l_char]

            l += 1    

            if s1Counts == s2Counts: return True

        return False    



      
            
