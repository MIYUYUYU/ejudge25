current_max = global_max = (x:=int(input()))
i = 1
while (x:=int(input())) != 0:
    current_max = max(current_max + x, x)
    global_max = max(global_max, current_max)
    #print (f"{i} : current_max = {current_max}, global_max = {global_max}, x = {x},")
    #i += 1
print(global_max)