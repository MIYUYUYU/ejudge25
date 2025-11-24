import sys
with open('output.bin','rb') as f:
    data = f.read()
    #print(data)

#data = sys.stdin.buffer.read()
    idx = data.find(b'\x00')
    if idx == -1:
        text_bytes = data
        fragments = []
    else:
        text_bytes = data[:idx]
        remaining = data[idx + 1:]
        fragments = [f for f in remaining.split(b'\x00') if f]

    text_str = text_bytes.decode('utf-8')

    encodings = ['cp866', 'cp1251', 'koi8_r', 'iso8859_5']

    for fragment in fragments:
        found = False
        for enc in encodings:
            try:
                s = fragment.decode(enc)
                if s in text_str:
                    print("Yes")
                    found = True
                    break
            except UnicodeDecodeError:
                continue
        if not found:
            print("No")

