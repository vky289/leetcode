class Solution(object):
    def __init__(self):
        self.solution = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        col, posDiag, negDiag = set(), set(), set()
        board = [['.'] * n for row in range(n)]
        
        def backTrack(r):
            if r==n:
                print(str(board))
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                backTrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backTrack(0)
        return res
        