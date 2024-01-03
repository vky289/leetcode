class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def is_safe(r, c, k, board):
            for i in range(9):
                if board[r][i] == k:
                    return False
                if board[i][c] == k:
                    return False
                if board[3*(r//3) + i // 3][3 * (c//3) + i % 3] == k:
                    return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1,10):
                            k = str(k)
                            if is_safe(i,j,k,board):
                                board[i][j] = k
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)
        return board