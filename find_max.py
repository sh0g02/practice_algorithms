# 配列の最大値を導く再帰関数
def find_max(max, arr):
    if arr == []:
        return max
    else:
        if max < arr[0]:
            max = arr[0]
        return find_max(max, arr[1:])

print(find_max(0, [1, 30, 4, 5]))