# リストの中の個数を導く再帰関数
def sum(arr):
    if arr == []:
        return 0
    else:
        return 1 + sum(arr[1:])

print(sum([1, 1, 1, 3, 4, 2, 3]))