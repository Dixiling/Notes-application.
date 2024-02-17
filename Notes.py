import json
import os
import datetime

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r") as file:
        return json.load(file)
    
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")
    
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