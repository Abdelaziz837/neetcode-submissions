class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ")" : "(" , 
            "}" : "{" , 
            "]" : "["
        }

        stack = []

        for c in s:
            if c in hmap:
               if not stack:
                   return False
               lastItem = stack[-1]

               if hmap[c] != lastItem:
                  return False

               stack.pop()

            else:
               stack.append(c)

        return len(stack) == 0       




