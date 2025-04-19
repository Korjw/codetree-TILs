n, t = map(int,input().split())

c = input()
grid = [list(map(int,input().split())) for _ in range(n)]
curr = [n // 2, n // 2]
dx, dy = [-1,0,1,0], [0,1,0,-1]
direction = 0
result = grid[curr[0]][curr[1]]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

for s in c:
    if s == 'L':
        direction = (direction -1) % 4
    elif s == 'R':
        direction = (direction +1) % 4
    else:
        if not out_of_range(curr[0]+dx[direction], curr[1]+dy[direction]):
            curr[0], curr[1] = curr[0]+dx[direction], curr[1]+dy[direction]
            result += grid[curr[0]][curr[1]]
print(result)