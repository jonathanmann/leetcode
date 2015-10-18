class Solution:

    """
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    """

    """
    0 : dead
    1 : alive
    2 : dying
    3 : spawing
    """

    def gameOfLife(self, board):
        self.board = board
        self.update_rules = {0:0,1:1,2:0,3:1}
        if board == []: return []
        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        for i,row in enumerate(self.board):
            i_opts = self.get_opts(i,self.num_rows)
            for j,col in enumerate(row):
                j_opts = self.get_opts(j,self.num_cols)
                pos = [i,j]
                nbs = self.get_neighbors(i_opts,j_opts,pos)
                self.update_tile_value(nbs,i,j)
        self.update_board()
        return self.board

    def update_board(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.board[i][j] = self.update_rules[self.board[i][j]]

    def update_tile_value(self,neighbors,i,j):
        if self.board[i][j] == 0:
            if neighbors == 3:
                self.board[i][j] = 3
        else:
            if neighbors not in [2,3]:
                self.board[i][j] = 2

    def get_opts(self,pos,lim):
        opts = [pos]
        if pos < lim - 1:
            opts.append(pos + 1)
        if pos > 0:
            opts.append(pos - 1)
        return opts

    def get_neighbors(self,row_opts,col_opts,pos):
        neighbors = 0
        for e in row_opts:
            for f in col_opts:
                if [e,f] != pos:
                    tile = self.board[e][f]
                    if tile in [1,2]:
                        neighbors += 1
        return neighbors

board = [[0,0,0],[1,0,0],[0,1,0]]
print Solution().gameOfLife(board)

board = [['00','01','02'],['10','11','12'],['20','21','22']]
board = [[0,1,0],[1,1,1],[0,1,0]]
board = [[1,1],[1,0]]
board = Solution().gameOfLife(board)
print board
