class Solution(object):
    def validate(self, row):
        track = {}
        for num in row:
            if num != '.':
                if num in track:
                    return False
                else:
                    track[num] = 1
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = True
        for row in board:
            flag = flag and self.validate(row)

        transpose_board = list(map(list, zip(*board)))

        for row in transpose_board:
            flag = flag and self.validate(row)

        i,j=0,0

        for i in range (0, 9, 3):
            for j in range (0, 9, 3):
                row = [
                    board[i][j], board[i][j+1], board[i][j+2],
                    board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                    board[i+2][j], board[i+2][j+1], board[i+2][j+2]
                ]
                flag = flag and self.validate(row)


        return flag
