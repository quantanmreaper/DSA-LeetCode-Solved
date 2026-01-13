class Solution:
    def setZeroes(self, matrix):
        """
        Brute Force Approach
        Time Complexity: O(m*n*(m+n))
        Space Complexity: O(1) with marker approach
        """
        n = len(matrix)      # number of rows
        m = len(matrix[0])   # number of columns
        
        # Define helper functions first
        def markRow(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1
                    
        def markCol(j):
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1
        
        # First pass: find zeros and mark their rows/columns
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    markRow(i)
                    markCol(j)
        
        # Second pass: convert all markers to 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Before:", matrix1)
    solution.setZeroes(matrix1)
    print("After:", matrix1)
    print("Expected: [[1,0,1],[0,0,0],[1,0,1]]")
    print()
    
    # Test case 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print("Before:", matrix2)
    solution.setZeroes(matrix2)
    print("After:", matrix2)
    print("Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]")
