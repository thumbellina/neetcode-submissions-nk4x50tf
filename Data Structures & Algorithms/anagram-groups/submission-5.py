# understand 
# Match
  # brute force O(N2)
  # sort O(N*KLogK)
  # 1 i have matching anagrams either get i into a array in first 
  # O(N*K) solution -> # use frequency array - ord - tuple
# Plan: loop once use frequency array tuple as key
# Execute
# review
# evaluate
from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_dic = defaultdict(list)

        for word in strs:
            key_arr = [0]*26

            for letter in word:
                key_arr[ord(letter)-ord('a')] += 1
            grouped_dic[tuple(key_arr)].append(word)
        return list(grouped_dic.values())


        

            
        
        