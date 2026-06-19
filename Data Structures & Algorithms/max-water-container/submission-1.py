class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        bestarea = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            a = w * h
            bestarea = max(a, bestarea)

            if h == heights[l]:
                l += 1
            else:
                r -= 1
        return bestarea
