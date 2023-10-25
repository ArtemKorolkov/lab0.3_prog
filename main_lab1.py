def calculator(str):
    m = list(str.split())
    if len(m)==3:
        a,zn,b=m[0],m[1],m[2]
        if zn == '+' and a.isnumeric() and b.isnumeric():
            return float(a) + float(b)
        elif zn == '-' and a.isnumeric() and b.isnumeric():
            return float(a) - float(b)
        elif zn == '*' and a.isnumeric() and b.isnumeric():
            return float(a) * float(b)
        elif zn == '/' and a.isnumeric() and b.isnumeric() and b!='0':
            return float(a) / float(b)
        elif zn == '//' and a.isnumeric() and b.isnumeric() and b!='0':
            return float(a) // float(b)
        elif zn == '%' and a.isnumeric() and b.isnumeric():
            return float(a) % float(b)
        else:
            return "Ошибка! Проверьте точность данных"
    else:
        return "Неверный формат ввода"


'''while True:
    print("Введите значения в формате: число знак(+,-,*,/,//,%) число")
    print("'Exit' для выхода")
    f=input()
    if f=='Exit':
        break
    else:
        print(calculator(f))'''

