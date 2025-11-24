with open('DOSGREP.flp', 'rb') as f:
    data = f.read()

    size_of_sector = 512
    offset_start = 512 * 19      #start+fat1+fat2
    offset_end = offset_start + size_of_sector * 14
    length = (offset_end - offset_start) // 32
    file_info = []
    for i in range(length):
        name_by = data[i * 32 + offset_start: i * 32 + offset_start + 8]
        ext_by = data[i * 32 + offset_start + 8: i * 32 + offset_start + 11]
        attr_by = data[i * 32 + offset_start + 11]
        size_of_file =  data[i * 32 + offset_start + 28: i * 32 + offset_start + 32]
        #print(f"{name_by=} {attr_by=}")
        if name_by[0] == 0x00:
            break
        if name_by[0] == 0xE5:
            continue
        if attr_by == 0x08:
            #print(1)
            continue

        name = name_by.decode('CP866').rstrip()
        ext = ext_by.decode('CP866').rstrip()
        #print(f'{name=} {ext=}')
        if ext == '':
            file_size = 'dir'
            filename = name
        elif ext == 'DIR':
            filename = name + '.' + ext
            file_size = 'dir'
        else:
            file_size = int.from_bytes(size_of_file, 'little')
            filename = name + '.' + ext
        file_info.append((filename, file_size))
    file_info.sort(key = lambda x: x[0], reverse = False)
    for file_ in file_info:
        print(f'{file_[0]} {file_[1]}')