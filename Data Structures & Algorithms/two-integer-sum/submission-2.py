class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)) :
            num = nums[i]
            newnum = target - num
            index = i

            if newnum in hashmap :
                return [hashmap[newnum] , index]

            hashmap[num] = i
        