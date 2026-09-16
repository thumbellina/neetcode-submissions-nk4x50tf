class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx,num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return sorted([idx,index_map[complement]])
            index_map[num] = idx



# understanding constraints: Is it sorted? only positive numbers? only index? no duplicates? 
# matching with examples 
    #1. bruteforce : nested loop O(N^2) 
    #2 sort the array and use two pointer if not O(Nlogn)
    #3 if unsorted loop once while using hashmap O(N) tc. #3
# planning pseudo code
#1 initiate hashmap with index as val and key the actual number
#2 loop through array save to hashmap if not there else check for complement if tehre return index 
         
# implementation
# review
# evaluate O(N) we traverse 1 time O(N) space
        