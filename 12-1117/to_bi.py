import re
import sys


def hexdump_to_binary(hexdump_text):
    # 提取所有十六进制字节
    hex_bytes = []
    for line in hexdump_text.split('\n'):
        if not line.strip():
            continue

        # 提取十六进制部分（跳过偏移量和ASCII可视化部分）
        hex_part = line[10:58] if len(line) > 58 else line[10:]
        hex_part = hex_part.strip()

        # 提取所有十六进制字节
        hex_values = re.findall(r'[0-9a-fA-F]{2}', hex_part)
        hex_bytes.extend(hex_values)

    # 转换为二进制数据
    binary_data = bytes.fromhex(''.join(hex_bytes))
    return binary_data
binary_data = hexdump_to_binary(sys.stdin.read())
with open('output.bin', 'wb') as f:
    f.write(binary_data)

print(f"已创建二进制文件，大小: {len(binary_data)} 字节")