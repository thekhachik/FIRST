# Задача:
# Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра. 
# В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None. 
# Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».

# Решение:
# Для начала необходимо задать ограничение на тип переменных (в нашем случае предполагаются строго ключевые аргументы). 
# Также, по условию сказано, что переменных может быть от одной до трех. 
# Поэтому двум последним параметрам присваиваем дефолтное значение None.
# Проще всего решить задачу использовав функцию locals(), которая в виде словаря представит все внутренние аргументы функции.

def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

three_args(var1=21)
three_args(var1='Python', var3=3)
three_args(var1='Python', var2=3, var3=9)

# Результат выполнения
# Переданы аргументы: var1 = 21
# Переданы аргументы: var1 = Python, var3 = 3
# Переданы аргументы: var1 = Python, var2 = 3, var3 = 9
