class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def BinarySearch(arr):
            start = 0
            end = len(arr)

            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    #The target is greater than the middle
                    #Go right
                    start = mid + 1
                else:
                    #Target less than the middle
                    #Go left
                    end = mid - 1
            return False

        for i in range(len(matrix)):
            if target < matrix[i][(len(matrix[i]) - 1)]:
                return BinarySearch(matrix[i])
            elif target == matrix[i][(len(matrix[i]) - 1)]:
                return True
        return False
            

