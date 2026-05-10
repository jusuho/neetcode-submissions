class Solution:
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(x, y, index):

            # 全部匹配成功
            if index == len(word):
                return True

            # 越界 or mismatch
            if (
                x < 0 or
                y < 0 or
                x >= cols or
                y >= rows or
                board[y][x] != word[index]
            ):
                return False

            # visited
            c = board[y][x]
            board[y][x] = "#"

            found = (
                dfs(x+1, y, index+1) or
                dfs(x-1, y, index+1) or
                dfs(x, y+1, index+1) or
                dfs(x, y-1, index+1)
            )

            # backtrack
            board[y][x] = c

            return found

        # 每格都當起點
        for y in range(rows):
            for x in range(cols):

                if dfs(x, y, 0):
                    return True

        return False