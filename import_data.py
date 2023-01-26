def get_data(path):
    data=input('Введите через запятую: ID, Имя, Фамилию, Номер телефона, Комментарий \n')
    filephone = open(path, 'a')
    filephone.writelines(data + '\n')
    filephone.close()
