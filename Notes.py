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

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note["title"] = title
            note["body"] = body
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с таким ID не найдена.")

  
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