import math

def min_square_size(N, W, H):
    if max(H, W) <= 2 * N:
        return max(H, W)
    sqr = math.sqrt(N)
    root = math.floor(sqr)
    left = True if sqr - root > 0 else False
    max_width = root * W + W if left and W <= H else root * W
    max_height = root * H + H if left and W >= H else root * H
    return max(max_width, max_height)




N, W, H = map(int, input().split())

result = min_square_size(N, W, H)
print(result)