import math
class Solution:
    @staticmethod
    def minimal_square_size(N, W, H):
        max_leaf_size = max(W, H)
        min_leaf_size = min(W, H)
        n_min = int(N ** 0.5)
        
        if n_min == 1:
            return N * min_leaf_size

        leafs_med = n_min * max_leaf_size
        leafs_min = N * min_leaf_size 
        leafs_max = N * max_leaf_size 
        
        min_side = min(leafs_min, leafs_max, leafs_med)
    
        return min_side 

    """ N, W, H = map(int, input().split())

    result = minimal_square_size(N, W, H)
    print(result) """