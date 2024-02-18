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

def show_note():
    note_id = int(input("Введите ID заметки для просмотра: "))
    for note in notes:
        if note["id"] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата создания: {note['date']}")
            return
    print("Заметка с таким ID не найдена.")

def show_date_notes():
    date = input("Введите дату в формате YYYY-MM-DD: ")
    filtered_notes = filter_notes_by_date(notes, date)
    for note in filtered_notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['date']}")

def filter_notes_by_date(notes, date):
    return [note for note in notes if note["date"].startswith(date)]


def show_notes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Дата создания: {note['date']}")

  
notes = load_notes()

user_input = None
while user_input != '7':
    print("\n1. Добавление заметки")
    print("2. Редактирование заметки")
    print("3. Удаление заметки")
    print("4. Поиск заметки по ID")
    print("5. Поиск заметки по дате")
    print("6. Показать список заметок")
    print("7. Выход")
    choice = input("Выберите действие: ")

    match choice:
        case  "1":
            add_note()
        case  "2":
            edit_note()
        case "3":
            delete_note()
        case  "4":
            show_note()
        case  "5":
            show_date_notes()
        case  "6":
            show_notes()
        case  "7":
            break
        case _:
            print("Неверный ввод.")