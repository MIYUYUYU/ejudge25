def No_2Zero(N, K):
    if N == 0:
       return 0
    if N == 1:
       return K - 1

    end_0 = 0
    end_not_0 = K - 1
    for i in range(1, N):
        new_ed_N0 = (end_0 + end_not_0) * (K - 1)
        new_end_0 = end_not_0
        end_not_0 = new_ed_N0
        end_0 = new_end_0
    return (end_0 + end_not_0)

# 测试示例
#print(No_22ero(33, 3))  # 输出: 328
