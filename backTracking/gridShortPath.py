grid = [
    [4, 5, 6, 8, 9],
    [2, 7, 1, 3, 6],
    [9, 4, 8, 2, 5],
    [3, 6, 7, 1, 4],
    [8, 2, 5, 9, 3],
]
n,m = 5, 5

def gridSmallpath(r, c):
    if r == n-1 and c == m-1:
        return grid[r][c]
    right = float('inf')
    if c+1 < m:
        right = gridSmallpath(r, c+1)
    down = float('inf')
    if r+1 < n:
        down = gridSmallpath(r+1, c)
    return grid[r][c] + min(right, down)

print(gridSmallpath(4,4))
print(gridSmallpath(0,0))