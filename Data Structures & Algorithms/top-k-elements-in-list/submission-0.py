class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:

            if num not in hashmap:
                count = 1
                hashmap[num] = count
            else:
                hashmap[num] += 1

        return sorted(hashmap , key = hashmap.get , reverse = True)[:k]     
