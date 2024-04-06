import json




while True:
    command = input("Введите команду: ")
    if command == "load":
        notes = load()
    elif command == "add":
        add_note()
    elif command == "help":
        help()
    elif command == "find":
        none = input("Введите заголовок заметки: ")
        if none in notes:
            print_note(none)
        else:
            print("Заметка с таким заголовком не найдена")
    elif command == "save":
        save()
    elif command == "edit":
        edit_note()
    elif command == "all":
        print_notes()
    elif command == "del":
        none = input("Введите заголовок заметки: ")
        if none in notes:
            del notes[none]
            print(f"Заметка \"{none}\" удалена")
        else:
            print("Заметка с таким заголовком не найдена")
        save()
    elif command == "exit":
        save()
        print("Вы вышли из приложения заметки")
        break
    else:
        print("Введена несуществующая команда, попробуйте еще раз")