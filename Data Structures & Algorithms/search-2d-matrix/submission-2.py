class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1] :
            return False
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                beg = 0
                end = n-1
                while beg <= end:
                    mid = (beg+end)//2
                    if matrix[i][mid] == target :
                        return True
                    
                    if target > matrix[i][mid] :
                        beg = mid+1
                    else :
                        end = mid -1


            else:
            
                continue
        return False