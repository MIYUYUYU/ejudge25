import sys

with open('DOSGREP.flp','rb') as f:
#data = sys.stdin.buffer.read()
    data = f.read()
    # Параметры образа (стандартные для 1.44 МБ дискеты)
    sector_size = 512
    root_dir_start = 19 * sector_size  # 19-й сектор
    root_dir_entries = 224
    entry_size = 32

    entries = []
    #print(data)
    for i in range(root_dir_entries):
        offset = root_dir_start + i * entry_size
        if offset + entry_size > len(data):
            break

        entry = data[offset:offset + entry_size]

        # Первый байт имени
        first_byte = entry[0]
        if first_byte == 0x00:  # Конец каталога
            break
        if first_byte == 0xE5:  # Удаленный файл
            continue

        # Атрибуты файла
        attr = entry[11]
        if attr & 0x08:  # Метка тома
            continue

        # Чтение имени (8 символов) и расширения (3 символа)
        name_bytes = entry[0:8]
        ext_bytes = entry[8:11]

        # Декодирование из CP866
        name = name_bytes.decode('cp866', errors='replace').rstrip()
        ext = ext_bytes.decode('cp866', errors='replace').rstrip()

        # Формирование полного имени
        filename = name + ('.' + ext if ext else '')

        # Определение типа записи
        if attr & 0x10:  # Каталог
            size_str = 'dir'
        else:
            size = int.from_bytes(entry[28:32], 'little')
            size_str = str(size)

        entries.append((filename, size_str))

    # Сортировка по имени файла
    entries.sort(key=lambda x: x[0])

    # Вывод результатов
    for filename, size in entries:
        print(f"{filename} {size}")
