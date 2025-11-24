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
length_to_now = 0
row = [Bord_style['vertical']]
tee_position_in_rows = {}
words_len = []
row_count = 0
output_words = []
for word in words:
    #print(f'{word=}')
    if length_to_now + len(word) + 1 >= size:
        row.append(' '*(size-1-length_to_now))
        if row[-1] != Bord_style['vertical']:
            row[-1],row[-2] = row[-2],row[-1]
        tee_position_in_rows[row_count] = words_len
        row_count += 1
        output_words.append(row)
        row = [Bord_style['vertical'],word,Bord_style['vertical']]
        length_to_now = len(word) + 1
        words_len = [length_to_now]
    else:
        row.append(word)
        row.append(Bord_style['vertical'])
        length_to_now += len(word) + 1
        words_len.append(length_to_now)
if row:
    row.append(' ' * (size - 1 - length_to_now))
    if row[-1] != Bord_style['vertical']:
        row[-1], row[-2] = row[-2], row[-1]
    tee_position_in_rows[row_count] = words_len
    row_count += 1
    output_words.append(row)
out_words = []
for row_word in output_words:
    row = ''.join(row_word)
    out_words.append(row)
#print(tee_position_in_rows)

border=[]
for _ in range(row_count + 1):
    border_row = [Bord_style['horizontal'] for _ in range(size)]
    border.append(border_row)
#print(border)
border[0][0] = Bord_style['top_left']
border[0][size - 1] = Bord_style['top_right']
border[row_count][0] = Bord_style['bottom_left']
border[row_count][size - 1] = Bord_style['bottom_right']
for j in range(len(tee_position_in_rows[0]) - 1):
    change_positions = tee_position_in_rows[0][j]
    border[0][change_positions] = Bord_style['top_tee']

for i in range(1, len(border) - 1):
    border[i][0] = Bord_style['left_tee']
    border[i][size - 1] = Bord_style['right_tee']
    for j in range(len(tee_position_in_rows[i-1]) - 1):
        change_positions_up = tee_position_in_rows[i-1][j]
        #print(f'{i=}{change_positions=}')
        border[i][change_positions_up] = Bord_style['bottom_tee']

        if j < len(tee_position_in_rows[i]):
            change_positions_down = tee_position_in_rows[i][j]
            #print(f'{i=} {change_positions_down=} {len(tee_position_in_rows[i])=}')
            border[i][change_positions_down] = Bord_style['top_tee']
        try:
            if change_positions_up in tee_position_in_rows[i]:
                border[i][change_positions_up] = Bord_style['cross']
        except IndexError:
            continue
for j in range(len(tee_position_in_rows[row_count-1]) - 1):
    change_positions = tee_position_in_rows[row_count-1][j]
    border[row_count][change_positions] = Bord_style['bottom_tee']
#print(len(tee_position_in_rows[0]))

out_border = []
for b in border:
    row = ''.join(b)
    out_border.append(row)
out_without_last = '\n'.join(['\n'.join(row) for row in zip(out_border[:-1], out_words)])
out_with_last = '\n'.join([out_without_last,out_border[-1]])
print(out_with_last)
#print(tee_position_in_rows)
#print(Bord_style)
