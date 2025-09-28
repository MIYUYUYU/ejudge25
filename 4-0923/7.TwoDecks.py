# A = [int(x.strip()) for x in input().split(',')]
# B = []
# for i in range(len(A)):
#     index = A.index(min(A))
#     B.append(A.pop(index))
#     print(B[i],end = ' ')
# # for b in B:
# #     print(b,end = ' ')
# 读取输入
A = [int(x.strip()) for x in input().split(',')]

# 归并排序（不使用函数）
if A:  # 确保列表非空
    # 初始化为单个元素的列表
    segments = [[x] for x in A]

    # 归并阶段
    while len(segments) > 1:
        new_segments = []
        i = 0
        while i < len(segments):
            if i + 1 < len(segments):
                # 合并两个相邻段
                left = segments[i]
                right = segments[i + 1]
                merged = []
                l_idx, r_idx = 0, 0

                # 合并两个有序列表
                while l_idx < len(left) and r_idx < len(right):
                    if left[l_idx] <= right[r_idx]:
                        merged.append(left[l_idx])
                        l_idx += 1
                    else:
                        merged.append(right[r_idx])
                        r_idx += 1

                # 添加剩余元素
                merged.extend(left[l_idx:])
                merged.extend(right[r_idx:])

                new_segments.append(merged)
                i += 2
            else:
                # 单独处理最后一个段（如果总段数为奇数）
                new_segments.append(segments[i])
                i += 1

        segments = new_segments
        print(f"segments = {segments}")

    # 最终结果
    B = segments[0]
else:
    B = []

# 输出结果
for b in B:
    print(b, end=' ')