class Solution:
    def encode(self, strs: List[str]) -> str:

        res = []

        if not strs:
            return ""

        for s in strs:
            res.append(f"{len(s)}#@{s}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
       
        while i < len(s):

            j = s.find("#@" , i)
            length_of_str = int(s[i:j])

            start_of_str = j + 2
            end_of_str = start_of_str + length_of_str

            res.append(s[start_of_str : end_of_str])

            i = end_of_str

        return res    







