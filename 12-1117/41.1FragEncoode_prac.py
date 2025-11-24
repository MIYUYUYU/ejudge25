import sys
with open('FragEncode', 'rb') as f:
    #data = f.read()
    #print(data)
    data = sys.stdin.buffer.read()
    ind = data.find(b'\x00')
    orig_txt = data[:ind].decode('utf-8')
    rest_txt = data[ind+1:]
    #print(ind)
    ind_F = rest_txt.find(b'\x00')

    # fragments = []
    # while ind_F != -1:
    #     fragments.append(rest_txt[:ind_F])
    #     rest_txt = rest_txt[ind_F+1:]
    #     ind_F = rest_txt.find(b'\x00')
    fragments = [f for f in rest_txt.split(b'\x00') if f]
    dec = ['CP866','CP1251','KOI8-R','ISO-8859-5']
    Find = False
    for fragment in fragments:
        for code_type in dec:
            try:
                fragment_after_decode = fragment.decode(code_type)
                if fragment_after_decode in orig_txt:
                    Find = True
                    break
            except UnicodeDecodeError:
                continue
        if Find:
            print("YES")
        else:
            print("NO")


