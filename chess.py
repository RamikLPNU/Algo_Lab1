from collections import deque

with open('input.txt', "r") as file:
    size = int(file.readline())
    start = tuple(map(int, file.readline().split(',')))
    end = tuple(map(int, file.readline().split(',')))

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

def is_valid(x, y, size):
    return 0 <= x < size and 0 <= y < size


def find_min_moves(size, start, end):
    visited = [[False] * size for _ in range(size)]
    queue = deque([(start[0], start[1], 0, [(start[0], start[1])])])
    iteration = 0
    while queue:

        iteration += 1
        x, y, moves, path = queue.popleft()

        if (x, y) == end:
            print(iteration)
            return moves, path

        for k in range(7):
            iteration += 1

            new_x = x + row[k]
            new_y = y + col[k]
            if is_valid(new_x, new_y, size) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1, path + [(new_x, new_y)]))


with open('output.txt', 'w') as file:
    moves, path = find_min_moves(size, start, end)
    file.write(str(moves))


