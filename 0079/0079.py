class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def backTrack(row, col, word):
            if len(word) == 0:
                return True

            if row < 0 or row == len(board) or col <0 or col == len(board[0]) \
                    or board[row][col].lower() != word[0].lower():
                return False

            board[row][col] = '*'

            for rowOffset, colOffset in [[1,0], [0,1], [-1,0], [0,-1]]:
                if backTrack(row+rowOffset, col + colOffset, word[1:]):
                    return True

            board[row][col] = word[0]

            return False
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if backTrack(i, j, word):
                    return True

        return False
