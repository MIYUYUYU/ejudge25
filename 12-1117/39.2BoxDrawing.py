import sys
import unicodedata

# 确保使用 UTF-8 编码输出
if sys.stdout.encoding != 'UTF-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # 对于较旧的 Python 版本
        import codecs

        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

words = sys.stdin.readline().strip().split(' ')
frame = sys.stdin.readline().split(' ')
size = int(frame[0])
vertical_style = frame[1].strip()
horizontal_style = frame[2].strip()


class BorderStyles:
    @classmethod
    def get_char(cls, vertical, horizontal, char_type):
        # 特殊处理混合粗细的情况
        if vertical != horizontal:
            if char_type == 'top_left':
                name = f"BOX DRAWINGS DOWN {vertical} AND RIGHT {horizontal}"
            elif char_type == 'top_right':
                name = f"BOX DRAWINGS DOWN {vertical} AND LEFT {horizontal}"
            elif char_type == 'bottom_left':
                name = f"BOX DRAWINGS UP {vertical} AND RIGHT {horizontal}"
            elif char_type == 'bottom_right':
                name = f"BOX DRAWINGS UP {vertical} AND LEFT {horizontal}"
            elif char_type == 'left_tee':
                name = f"BOX DRAWINGS VERTICAL {vertical} AND RIGHT {horizontal}"
            elif char_type == 'right_tee':
                name = f"BOX DRAWINGS VERTICAL {vertical} AND LEFT {horizontal}"
            elif char_type == 'top_tee':
                name = f"BOX DRAWINGS DOWN {vertical} AND HORIZONTAL {horizontal}"
            elif char_type == 'bottom_tee':
                name = f"BOX DRAWINGS UP {vertical} AND HORIZONTAL {horizontal}"
            elif char_type == 'cross':
                name = f"BOX DRAWINGS VERTICAL {vertical} AND HORIZONTAL {horizontal}"
            elif char_type == 'horizontal':
                name = f"BOX DRAWINGS {horizontal} HORIZONTAL"
            elif char_type == 'vertical':
                name = f"BOX DRAWINGS {vertical} VERTICAL"
        else:
            # 相同粗细的情况
            if char_type == 'top_left':
                name = f"BOX DRAWINGS {vertical} DOWN AND RIGHT"
            elif char_type == 'top_right':
                name = f"BOX DRAWINGS {vertical} DOWN AND LEFT"
            elif char_type == 'bottom_left':
                name = f"BOX DRAWINGS {vertical} UP AND RIGHT"
            elif char_type == 'bottom_right':
                name = f"BOX DRAWINGS {vertical} UP AND LEFT"
            elif char_type == 'left_tee':
                name = f"BOX DRAWINGS {vertical} VERTICAL AND RIGHT"
            elif char_type == 'right_tee':
                name = f"BOX DRAWINGS {vertical} VERTICAL AND LEFT"
            elif char_type == 'top_tee':
                name = f"BOX DRAWINGS {vertical} DOWN AND HORIZONTAL"
            elif char_type == 'bottom_tee':
                name = f"BOX DRAWINGS {vertical} UP AND HORIZONTAL"
            elif char_type == 'cross':
                name = f"BOX DRAWINGS {vertical} VERTICAL AND HORIZONTAL"
            elif char_type == 'horizontal':
                name = f"BOX DRAWINGS {vertical} HORIZONTAL"
            elif char_type == 'vertical':
                name = f"BOX DRAWINGS {vertical} VERTICAL"

        return unicodedata.lookup(name.strip())
    @classmethod
    def get_style(cls, vertical, horizontal):
        style = {}
        for char_type in ['horizontal', 'vertical', 'top_left', 'top_right',
                          'bottom_left', 'bottom_right', 'left_tee', 'right_tee',
                          'top_tee', 'bottom_tee', 'cross']:
            style[char_type] = cls.get_char(vertical, horizontal, char_type)
        return style

Bord_style = BorderStyles.get_style(vertical_style, horizontal_style)
#print(Bord_style)
# 重新设计单词分配和边框生成逻辑
lines = []
current_line = []
current_length = 0

for word in words:
    # 计算添加这个单词后的长度（包括分隔符）
    if current_length == 0:
        new_length = len(word)
    else:
        new_length = current_length + 1 + len(word)

    # 如果添加后不超过宽度，则添加到当前行
    if new_length <= size - 2:  # -2 是为了左右边框
        current_line.append(word)
        current_length = new_length
    else:
        # 开始新行
        if current_line:
            lines.append(current_line)
        current_line = [word]
        current_length = len(word)

# 添加最后一行
if current_line:
    lines.append(current_line)

# 生成输出行和分隔符位置
output_lines = []
separator_positions = []

for line in lines:
    # 计算需要的空格数
    total_chars = sum(len(word) for word in line) + len(line) - 1
    spaces_needed = (size - 2) - total_chars

    # 构建行内容
    line_content = Bord_style['vertical']
    positions = []
    pos = 0

    for i, word in enumerate(line):
        line_content += word
        pos += len(word)

        if i < len(line) - 1:
            line_content += Bord_style['vertical']
            positions.append(pos)
            pos += 1  # 分隔符位置
        else:
            line_content += ' ' * spaces_needed + Bord_style['vertical']

    output_lines.append(line_content)
    separator_positions.append(positions)

# 生成边框行
border_lines = []

# 顶行
top_row = [Bord_style['top_left']]
for i in range(size - 2):
    if i in separator_positions[0]:
        top_row.append(Bord_style['top_tee'])
    else:
        top_row.append(Bord_style['horizontal'])
top_row.append(Bord_style['top_right'])
border_lines.append(''.join(top_row))

# 中间行
for i in range(len(lines) - 1):
    middle_row = [Bord_style['left_tee']]

    for j in range(size - 2):
        if j in separator_positions[i] and j in separator_positions[i + 1]:
            middle_row.append(Bord_style['cross'])
        elif j in separator_positions[i]:
            middle_row.append(Bord_style['bottom_tee'])
        elif j in separator_positions[i + 1]:
            middle_row.append(Bord_style['top_tee'])
        else:
            middle_row.append(Bord_style['horizontal'])

    middle_row.append(Bord_style['right_tee'])
    border_lines.append(''.join(middle_row))

# 底行
bottom_row = [Bord_style['bottom_left']]
for i in range(size - 2):
    if i in separator_positions[-1]:
        bottom_row.append(Bord_style['bottom_tee'])
    else:
        bottom_row.append(Bord_style['horizontal'])
bottom_row.append(Bord_style['bottom_right'])
border_lines.append(''.join(bottom_row))

# 交替输出边框行和内容行
result = []
for i in range(len(output_lines)):
    result.append(border_lines[i])
    result.append(output_lines[i])
result.append(border_lines[-1])

# 输出结果
print('\n'.join(result))
