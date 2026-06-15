class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = []

        for num in nums :

            if num in unique_num:
                return True

            unique_num.append(num)

        return False    
