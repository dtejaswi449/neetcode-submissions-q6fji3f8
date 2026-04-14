class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0 
        fresh = 0
        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    else:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1



