class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m=len(board),len(board[0])
        seen=set()
        def dfs(row,col):
            if (row,col) in seen:
                return
            seen.add((row,col))
            if row<0 or col<0 or row>n-1 or col>m-1 or board[row][col]=="X":
                return 
            board[row][col]="T"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    if board[i][j]=="O":
                        dfs(i,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"

            
        