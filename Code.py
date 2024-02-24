with open("phonebook.txt", "a+") as file:

    def write_data(name, surname, phone_number, address):
        file.write(f"{name},{surname},{phone_number},{address}\n")


    def read_data():
        file.seek(0)
        for line in file:
            print(line)


    def delete_data():
        file.truncate(0)


    while True:
        choice = input("Введите код действия (1 - записать данные, 2 - прочитать данные, 3 - удалить данные): ")

        if choice == "1":
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            address = input("Введите адрес: ")
            write_data(name, surname, phone_number, address)
        elif choice == "2":
            read_data()
        elif choice == "3":
            delete_data()
        else:
            print("Неверный код действия. Попробуйте снова.")