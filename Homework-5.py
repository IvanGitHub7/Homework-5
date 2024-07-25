# Создание неизменяемых структур даных
immutable_var = 1, 2, 'string', True
print('Неизменяемый кортеж: ', immutable_var)

# immutable_var[0] = 3 Выполнение данной строки пиведет к ошибке, т.к. элементы кортежа не подлежат изменению
#print(immutable_var)

# Создание изменяемых структур данных
mutable_list = ([1, 2, 3],True)
print('Кортеж с изменяемым элементом до изменнеий: ', mutable_list)
mutable_list[0][0] = 2
mutable_list[0][1] = 'Two'
print('Кортеж с изменяемым элементом после изменнеий: ', mutable_list)
