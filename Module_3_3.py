def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(26, 'Zero', False)
print_params(12, True) # третий параметр будет по умолчанию
print_params('Finish') #второй и третий параметр будет по умолчанию
print_params() # все параметры по умолчанию
print_params(b=25) # заменен только второй параметр, остальные по умолчанию
print_params(c = [1,2,3]) # третий параметр заменен на список

# Распаковка списка и словаря
values_list = ['Mom', 64, 28.8]
values_dict = {'a': 288, 'b': 'Ocean', 'c': False}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list2 = ['Мир', 288.5]
print_params(*values_list2, 42)
