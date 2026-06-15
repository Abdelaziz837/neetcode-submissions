class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            value = tuple(sorted(word))

            if value not in hashmap:
                hashmap[value] = [word] 
            else:
                hashmap[value].append(word)

        return list(hashmap.values())