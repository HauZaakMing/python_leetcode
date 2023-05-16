from typing import List
import numpy as np
import queue

class Solution:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    board = []

    def exist(self, board: List[List[str]], word: str) -> bool:
        len1 = len(board)
        len2 = len(board[0])
        self.board = board
        for i in range(len1):
            for j in range(len2):
                if board[i][j] == word[0]:
                    # dfs
                    board[i][j] = '#'
                    flag = self.dfs_word(i,j,1,word)
                    if flag:
                        return True
                    else:
                        board[i][j] = word[0]
        return False

    def dfs_word(self, x:int,y:int,cur:int,word:str)->bool:
        if cur == len(word) :
            return True
        for i in range(4):
            x_next = x + self.dirs[i][0]
            y_next = y + self.dirs[i][1]
            if x_next<0 or x_next>= len(self.board) or y_next<0 or y_next>= len(self.board[0]) or self.board[x_next][y_next]==1 or self.board[x_next][y_next]!=word[cur] :
                continue
            else:
                self.board[x_next][y_next] = '#'
                flag = self.dfs_word(x_next,y_next,cur+1,word)
                if flag :
                    return True
                self.board[x_next][y_next] = word[cur]


        return False

s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")

