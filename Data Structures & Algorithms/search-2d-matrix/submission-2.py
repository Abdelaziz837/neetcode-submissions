class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Length_rows = len(matrix)
        desired_row = -1

        for i in range(Length_rows):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                desired_row = i - 1
                break
            
        else:
            desired_row = Length_rows - 1

        arr = matrix[desired_row]
        r = len(arr) - 1
        l = 0

        while l <= r:
            middle = l + (r - l) // 2

            if arr[middle] == target:
                return True
            elif arr[middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False
