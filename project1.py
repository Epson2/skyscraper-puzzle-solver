#main function to set up dictionary and grid
def visible_number(N, clues):
    top, bottom, left, right = clues["top"], clues["bottom"], clues["left"], clues["right"]
    grid = [[0]*N for _ in range(N)]
    used_row = [set() for _ in range(N)]
    used_col = [set() for _ in range(N)]

    #function to count visible numbers
    def vis(seq):
        m = 0; seen = 0
        for v in seq:
            if v > m: m = v; seen += 1
        return seen

    #checks if row satisfies our clues left and right
    def row_check(r):
        row = grid[r]
        if 0 in row: return True
        if left[r]  and vis(row)       != left[r]:  return False
        if right[r] and vis(row[::-1]) != right[r]: return False
        return True

    #checks if column statisfies are clues top and bottom
    def col_check(c):
        col = [grid[r][c] for r in range(N)]
        if 0 in col: return True
        if top[c]    and vis(col)       != top[c]:    return False
        if bottom[c] and vis(col[::-1]) != bottom[c]: return False
        return True

    #DFS algorith to fill our grid cell by cell
    def dfs(r=0, c=0):
        if r == N: return True
        nr, nc = (r, c+1) if c+1 < N else (r+1, 0)

        for v in range(1, N+1):
            if v in used_row[r] or v in used_col[c]:
                continue
            grid[r][c] = v; used_row[r].add(v); used_col[c].add(v)
            if ((c < N-1 or row_check(r)) and (r < N-1 or col_check(c)) and dfs(nr, nc)):
                return True
            used_row[r].remove(v); used_col[c].remove(v); grid[r][c] = 0
        return False

    return grid if dfs(0) else None

#reader to read input from standard input
if __name__ == "__main__":
    import sys
    it = iter(sys.stdin.read().strip().splitlines())
    N = int(next(it).strip())
    top    = list(map(int, next(it).split()))
    bottom = list(map(int, next(it).split()))
    left   = list(map(int, next(it).split()))
    right  = list(map(int, next(it).split()))
    sol = visible_number(N, {"top": top, "bottom": bottom, "left": left, "right": right})
    if not sol:
        print("No solution")
    else:
        for row in sol:
            print(*row)
