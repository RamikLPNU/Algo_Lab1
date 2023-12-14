def subsets(nums):
    result = []
    sub_set = []

    def dfs(i):
        if i >= len(nums):
            result.append(sub_set.copy())
            return

        sub_set.append(nums[i])
        dfs(i + 1)

        sub_set.pop()
        dfs(i + 1)

    dfs(0)
    return result[::-1]

 
def solution(N, B, like_be):
    result = B
    like_be = like_be.split(" ")
    chosen_subset = []
    beers_subsets = subsets([i for i in range(B)])

    for subset in beers_subsets:
        zerous = [0 for _ in range(N)]

        for i, val in enumerate(like_be):
            for j in range(len(val)):
                if val[j] == "Y" and j in subset:
                    zerous[i] += 1

        if 0 not in zerous:
            result = min(result, len(subset))
            if result == len(subset):
                chosen_subset = subset

    return result 


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        N, B = map(int, lines[0].split())
        like_be = " ".join(lines[1:]).strip()

if __name__ == "__main__":
    main()