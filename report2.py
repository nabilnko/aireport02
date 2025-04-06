from typing import List, Tuple

class MazeSolverIDDFS:
    def __init__(self, maze: List[List[int]], start: Tuple[int, int], target: Tuple[int, int]):
        self.maze = maze
        self.start = start
        self.target = target
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0
        self.traversal_order = []
        self.correct_path = []

    def is_valid(self, x, y, visited):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0 and not visited[x][y]

    def dls(self, x, y, depth, limit, visited, path):
        if depth > limit:
            return False

        visited[x][y] = True
        path.append((x, y))
        self.traversal_order.append((x, y))

        if (x, y) == self.target:
            self.correct_path = list(path)
            return True

        directions = [(-1,0), (1,0), (0,-1), (0,1)] 

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, visited):
                if self.dls(nx, ny, depth + 1, limit, visited, path):
                    return True

        path.pop()
        visited[x][y] = False
        return False

    def iddfs(self, max_depth):
        for limit in range(max_depth + 1):
            visited = [[False] * self.cols for _ in range(self.rows)]
            path = []
            self.traversal_order.clear()
            if self.dls(self.start[0], self.start[1], 0, limit, visited, path):
                depth_found = len(self.correct_path) - 1  
                print(f"Path found at depth {depth_found} using IDDFS")
                print(f"Traversal Order: {self.correct_path}")
                return
        print(f"Path not found at max depth {max_depth} using IDDFS")


if __name__ == "__main__":
    maze1 = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1]
    ]
    start1 = (0, 0)
    target1 = (2, 3)
    solver1 = MazeSolverIDDFS(maze1, start1, target1)
    solver1.iddfs(15)

    print("\n")

    
    maze2 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    start2 = (0, 0)
    target2 = (2, 2)
    solver2 = MazeSolverIDDFS(maze2, start2, target2)
    solver2.iddfs(6)