class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # bruteforce find product of all elements loop and divide by 
        # the element to get product
        
        # first pass prefix prod
        res = [1]*len(nums)
        prefix =1
        for idx,num in enumerate(nums):
            # populate result array with prefix
            res[idx] *= prefix
            prefix *= num
        print(res)
        # reverse pass
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

        

    

        
        