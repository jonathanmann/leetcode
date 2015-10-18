

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
        if board == []: return []
        num_rows = len(board)
        num_cols = len(board[0])
        for i,row in enumerate(board):
            i_opts = self.get_opts(i,num_rows)
            for j,col in enumerate(row):
                j_opts = self.get_opts(j,num_cols)
                pos = [i,j]
                check_list = self.get_adjacent(i_opts,j_opts,pos)
                adj_sum = 0

                col_list = [] # for checking

                for e in check_list:
                    x,y = e
                    tile = board[x][y]
                    if tile == 1 or tile == 2:
                        adj_sum += 1

                    col_list.append(board[x][y]) # for checking
                print adj_sum
                print col_list # for checking

    def get_opts(self,pos,lim):
        opts = [pos]
        if pos < lim - 1:
            opts.append(pos + 1)
        if pos > 0:
            opts.append(pos - 1)
        return opts

    def get_adjacent(self,row_opts,col_opts,pos):
        adj = []
        for e in row_opts:
            for f in col_opts:
                if [e,f] != pos:
                    adj.append([e,f])
        return adj

board = [['00','01','02'],['10','11','12'],['20','21','22']]
board = [[0,1,0],[1,1,0],[0,1,0]]
Solution().gameOfLife(board)
