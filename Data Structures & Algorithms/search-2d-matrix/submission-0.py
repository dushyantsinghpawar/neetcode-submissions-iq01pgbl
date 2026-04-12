class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l, r = 0, m - 1
        
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] == target or matrix[m][n - 1] == target:
                return True

            if matrix[m][0] < target < matrix[m][n - 1]:
                li = 0
                ri = n - 1
                
                while li <= ri:
                    mi = (li + ri) // 2
                    if matrix[m][mi] == target:
                        return True
                    elif matrix[m][mi] < target:
                        li = mi + 1
                    else:
                        ri = mi - 1
                return False

            elif matrix[m][n - 1] < target:
                l = m + 1
            else:
                r = m - 1
        return False
