def evalform(formula, *args):
     variable = []
     current_var = ""
     for char in formula:
         if char.isalpha():
             current_var += char
         else:
             if current_var:
                variable.append(current_var)
                current_var = ""
     if current_var:
        variable.append(current_var)
     sorted_variable = sorted(set(variable))
     var_dic = dict(zip(sorted_variable, args))
     # print(var_dic)
     # print(args)
     # print(formula)
     return eval(formula, var_dic)


# namespace = {'a': 11, 'b' : 3, 'c': 2}
# str = "b*2 + a*3 + b//3 + c"

#print(namespace)
# a = input()
#print(eval(input()))
#print(eval(str,namespace))
print(*evalform("f(x)", sorted, "blahblah"))