class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_ = {}
        for idx,i in enumerate(nums):
            reminder = target - i
            if (reminder in check_) and (idx != check_[reminder]):
                return sorted([idx,check_[reminder]])
            check_[i] = idx
        
            
            




        