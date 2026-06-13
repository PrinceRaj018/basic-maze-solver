maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

row = 2
col = 2

goal_row = 2
goal_col = 0

print(row, col)

def check_position(row, col):
    if maze[row][col] == 1:
        print("Wall")
    else:
        print("Path")

check_position(row, col)

def solve(row, col):

    if row > 2:
        return

    print(row, col)

    if row == goal_row and col == goal_col:
        print("Goal Reached")
        return

    solve(row + 1, col)
solve(0,0)
