segments = [[int(x.strip())] for x in input().split(',')]

while len(segments) > 1:
    new_segments = []
    #print(i)
    for i in range(0,len(segments),2):
            if i + 1 < len(segments):
                #确定有下一个相邻碎片
                lft_idx = rgt_idx = 0
                merged = []

                #合并相邻2个碎片
                while lft_idx < len(segments[i]) and rgt_idx < len(segments[i + 1]):
                    if segments[i][lft_idx] < segments[i + 1][rgt_idx]:
                        merged.append(segments[i][lft_idx])
                        lft_idx += 1
                    else:
                        merged.append(segments[i + 1][rgt_idx])
                        rgt_idx += 1

                #合并相邻两个碎片中的剩余元素
                merged.extend(segments[i][lft_idx:])
                merged.extend(segments[i + 1][rgt_idx:])

                new_segments.append(merged)
                #print(f'segments = {segments} merged = {merged}')
            else:
                #合并单数最后一个碎片
                new_segments.append(segments[i])
                i += 1
            #print(f'new segments: {new_segments}')
    #重置循环初始列表
    segments = new_segments
    # print(f"segments = {segments}")
    # print(len(segments) > 1)

Output = segments[0]
for x in Output:
    print(x,end = ' ')