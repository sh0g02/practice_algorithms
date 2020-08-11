def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:]) # インデックス番号が1の要素から最後の要素までを1度に取得

print(sum([1, 3, 4, 5]))