def LookSay():
    tmp = [1]
    yield tmp[0]

    output = []
    index = 0
    while True:
        example = tmp[0]
        count_ex = 1
        start = index
        for i in range(1,len(tmp)):
            if tmp[i] == example:
                #print(f"tmp[i] = {tmp[i]}")
                count_ex += 1
            else:
                output.append(count_ex)
                output.append(example)
                for _ in range(2):
                    yield output[index]
                    index += 1
                example = tmp[i]
                count_ex = 1
        output.append(count_ex)
        output.append(example)
        for _ in range(2):
            yield output[index]
            index += 1
        end = index
        tmp = output[start:end + 1]
        #print(f"start = {start} end = {end} tmp = {tmp}")

# for i, l in enumerate(LookSay()):
#     print(f"{i}: {l}")
#     if i > 20:
#         break