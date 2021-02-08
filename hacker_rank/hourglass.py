def hourglassSum(arr):
    hg_sums = []
    for i in range(4):
        for j in range(4):
            hg_sums.append(sum(arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j+3]))
    return max(hg_sums)