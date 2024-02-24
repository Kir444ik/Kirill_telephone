from data_creat import name_data,surname_data,phone_data,address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input("В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))   

    
    while var != 1 and var != 2 and var != 3:
        print("Неправильно")
        var = int(input('ведите число'))
    
    if var == 1:
        with open('data_first_variant.csv', 'a' , encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_first_variant.csv', 'a' , encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")
    elif var == 3:
        with open('data_first_variant.csv' , 'a',encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r',encoding = 'utf-8' ) as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r',encoding = 'utf-8' ) as f:
        data_second = f.readlines()
        print(data_second)

def delit_data():
    print("Фамилию кого хотите заменить:")
    surname_new = input()
    print("Имя кого хотите заменить:")
    name_new = input()
    m = []
    with open('data_first_variant.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            name, surname, phone, address = line.strip().split(',')
            if name == name_new  and surname == surname_new:
                m.append(f"{name_data},{surname_data},{phone_data},{address_data}\n")
    
    with open('data_first_variant.csv', 'w') as file:
        file.writelines(m)
  
        
        