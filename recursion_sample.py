def countDown(i):
    print(i)
    if i <= 0:
        # 終了条件
        return
    else:
        # 終了条件に当てはまらない場合、再起呼び出し
        countDown(i - 1)

countDown(10)