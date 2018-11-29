# Нужно реализовать Польскую нотацию для двух положительных чисел.

expr = input('Введите выражение через пробел: ').split()

def calc(list):
    stack = []
    operator = ''
    for x in expr:
        if x.isdigit():
            stack.append(int(x))
            continue
        else:
            operator = x
            continue
    op1 = stack.pop()
    op2 = stack.pop()
    if operator == '+':
        print(op1 + op2)
    elif operator == '-':
        print(op2 - op1)
    elif operator == '*':
        print(op1 * op2)
    else:
        print(op2 // op1)
calc(expr)


# С помощью выражения assert проверять, что числа положительные.
# С помощью конструкций try/expcept ловить ошибки и выводить предупреждения

num = int(input('Введите положительное число: '))
try:
    assert num > 0
except AssertionError:
    print('Ошибка. Разрешен ввод только положительных чисел')



# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных»
# новой функцией, выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте,
# если поле "name" и документа.

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006"}
]


def find_name(documents):
  for document in documents:
    try:
        print("Документ №{}. Владелец: {}" .format(document["number"], document["name"]))
    except KeyError:
        print("Информация по имени отсутствует")

find_name(documents)


