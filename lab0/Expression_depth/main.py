def depth(exp, count=0):
    temp_dep = [0]
    if(isinstance(exp, (list, tuple))):
        count = count + 1
        for x in exp:
            temp_dep.append(depth(x))
    return count+max(temp_dep)


print(depth('x'))
print(depth(('expt', 'x', 2)))
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))
