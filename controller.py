import import_data
import export

def start():
    a= input("Введите W - если нужно записать данные, R -если необходимо прочитать\n")
    path = 'C:/Учеба/Python/file.txt'
    if a=="R"or a=="r":
        export.export_data(path)
    else:
        import_data.get_data(path)

