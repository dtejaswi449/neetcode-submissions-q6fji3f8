class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        def bfs(row, col):
            temp = 1
            grid[row][col] = 0
            q = collections.deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    elif grid[nr][nc] == 1:
                        temp += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return temp
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, (bfs(i, j)))
        return res