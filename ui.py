from loli import input_data,print_data,delit_data

def interface():
    print("Добрый день \n 1 - запись данных \n 2 - вывод данных \n 3 - перезаписать")
    command = int(input())

    while command != 1 and command != 2 and command != 3:
        print("Неправильно")
        command = int(input('ведите число'))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delit_data()