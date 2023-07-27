import Repository.loadFromFile as lF
import Repository.writeToFile as wF
import Models.Note


def add_note():
    title = input("Введите название заметки:\n")
    body = input("Введите текст заметки:\n")
    note = Models.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Models.Note.Note.get_id(note) == Models.Note.Note.get_id(i):
            Models.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена!")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("Программа для ведения журнала Заметок:")
            for i in array_notes:
                print(Models.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Models.Note.Note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == Models.Note.Note.get_id(i):
                    print(Models.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату заметки в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Models.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Models.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Дата не существует")
        else:
            print("Заметки не найдены!")


def del_notes():
    id = input("Введите ID заметки для удаления: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Models.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка : ", id, " удалена!")
    else:
        print("id не найден")


def change_note():
    id = input("Введите ID заметки: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Models.Note.Note.get_id(i):
            i.title = input("измените название:\n")
            i.body = input("измените текст:\n")
            Models.Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Заметка ", id, " изменена!")
    else:
        print("id не найден")








