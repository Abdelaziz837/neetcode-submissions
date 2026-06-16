class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # postfix and prefix arrays are the answer

        res = []
        prefix = 1 

        for i in range(len(nums)):

            res.append(prefix)
            prefix *= nums[i]

        postfix = 1 

        for i in range(len(nums) - 1 , -1 , -1):

            res[i]  *= postfix
            postfix  *= nums[i]

        return res        