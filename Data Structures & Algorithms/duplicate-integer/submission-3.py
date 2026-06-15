class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_num = {}

        for i in range(len(nums)):

            if nums[i] in unique_num:
                return True
            
            unique_num[nums[i]] = i

        return False        
