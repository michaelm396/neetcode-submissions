class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            m = (left + right) // 2
            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        return False
        