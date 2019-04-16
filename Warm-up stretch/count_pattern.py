import re


def count_pattern(pattern, exp):
    return len(re.findall('(?='+''.join(pattern)+')', ''.join(exp)))


res = count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'))
print(res)
