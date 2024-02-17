
notes = load_notes()

while True:
    print("\n1. Добавление заметки")
    print("2. Редактирование заметки")
    print("3. Удаление заметки")
    print("4. Поиск заметки по ID")
    print("5. Поиск заметки по дате")
    print("6. Показать список заметок")
    print("7. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        show_note()
    elif choice == "5":
        show_date_notes()
    elif choice == "6":
        show_notes()
    elif choice == "7":
        break
    else:
        print("Неверный ввод.")