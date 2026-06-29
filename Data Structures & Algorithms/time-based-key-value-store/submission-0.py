class TimeMap:

    def __init__(self):
        self.hashtable = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashtable[key].append((timestamp , value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashtable:
            return ""

        pairs = self.hashtable[key]

        l = 0
        r = len(pairs) - 1
        res = ""

        while l <= r :

            mid = (r + l) // 2

            if pairs[mid][0] <= timestamp :
                res = pairs[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res            

            

             
    
        
