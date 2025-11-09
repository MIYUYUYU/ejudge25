class MyException(Exception):
    def __init__(self, value):
            super().__init__(value)

inp = []
while True:
    inp_row = input()
    if inp_row == '':
        break
    else:
        inp.append(inp_row)

names = []
to_whos = []
for row in inp:
    n, t = row.split(':')
    names.append(n.strip())
    t = [t.strip() for t in t.split(', ')]
    to_whos.append(t)

#print(f'{names=}\n{to_whos=}')
dic_plan = dict(zip(names,to_whos))
#print(dic_plan)
def process_data():
    already_quest = set()
    for name, to_who in dic_plan.items():
        for who in to_who:
            #print(f'{who=}')
            if not who:
                continue
            if who not in names:
                raise MyException("UNKNOWN")
            elif name in dic_plan[who]:
                raise MyException("CYCLE")
            elif who in already_quest:
                raise MyException("INEFFECTIVE")
            already_quest.add(who)

    for name, to_who in dic_plan.items():
        for who in to_who:
            if not who:
                continue
            for who2 in dic_plan[who]:
                if who2 not in to_who and who2 != '':
                    to_who.append(who2)
        str1 = ', '.join(to_who)
        print(f'{name}: {str1}')
    #print(dic_plan)


try:
    process_data()
except MyException as e:
    print(f"{e}")