def quick_sort(list):
    if len(list) < 2:
        # 基本ケース、この場合はソート不要
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot] # pivotよりも小さい要素をすべて含んだ部分配列
        more = [i for i in list[1:] if i > pivot] # pivotよりも大きい要素をすべて含んだ部分配列
        return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort([10, 44, 5, 6, 78, 1]))