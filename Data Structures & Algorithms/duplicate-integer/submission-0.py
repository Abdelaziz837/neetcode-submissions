class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniquelist = []

        for x in nums:

            if x in uniquelist:
                return True

            uniquelist.append(x)

        return False
