class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][-1]:
                break
        else:
            return False
        for j in range(len(matrix[i])):
            if matrix[i][j]==target:
                return True
                break
        else:
            return False



        