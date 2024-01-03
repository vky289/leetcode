class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """


        def dfs(row, col, oldColor):
            row_len = len(image)
            col_len = len(image[0])

            for rowOffset, colOffset in [[0,1], [1, 0], [0,-1],[-1,0]]:
                i = row + rowOffset
                j = col + colOffset

                if i >= 0 and i < row_len and j >=0 and j < col_len and image[i][j] == oldColor:
                    image[i][j] = color
                    dfs(i, j, oldColor)


        if image[sr][sc] == color:
            return image
        else:
            oldColor, image[sr][sc] = image[sr][sc], color
            dfs(sr, sc, oldColor)

        return image