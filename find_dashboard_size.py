import math

def min_square_size(N, W, H):
    count = 0
    left, right = 1, max(W, H) * N

    while left < right:
        count += 1
        mid = (left + right) // 2
        sheets_per_row = mid // W
        sheets_per_col = mid // H
        total_sheets = sheets_per_row * sheets_per_col

        if total_sheets >= N:
            right = mid
        else:   
            left = mid + 1 


    return left, count


N, W, H = map(int, input().split())

result = min_square_size(N, W, H)
print(result)