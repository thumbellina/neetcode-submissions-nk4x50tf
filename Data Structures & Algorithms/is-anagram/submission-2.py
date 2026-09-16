# Understand # only smallcase letetrs? only english alphabets?
# Match and testcase 
#1  brute force nested loop O(N^2)
#2 sort and check if theya are equal O(NlogN)
#3 save in hashmap 2 sequential loops
# Plan pseudocode
# initiate hashmap freq_map_s
# loop through s and get s
# if not there return false 
# else loop through t and subtract check if 0 
# implement
# review. pool loop
# eval
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {} # p:0, o:0, l:0
        for alpha1 in s:
            if alpha1 in freq_map:
                freq_map[alpha1] += 1
            else:
                freq_map[alpha1] = 1
        
        for alpha2 in t:
            if alpha2 not in freq_map:
                return False
            else:
                freq_map[alpha2] -= 1

        for num in freq_map.values():
            if num != 0:
                return False
        return True



        