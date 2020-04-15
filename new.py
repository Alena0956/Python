# если ввведено имя с большой буквы-похвалить
# если с маленькой - строка 'bad gay'
# если имя введено с большой буквы и из списка  'Hi, again!'
# если с маленькой из списка или число - вывести ошибку
our_client = ['Sam', 'Ron', 'Harri', 'Jon', 'Genri']
while True:
    name = input('Enter your name with big letter, please:')
    if name == 'q':
        break
    if name == name.capitalize():
        print('You are diligent guy,', name, '!')
    if name == name.lower():
        print('You are very bad guy,', name, '((')
    if name == name.capitalize():
        if name in our_client:
            print('Hi again, mr.', name, '!')
    try:
        if name == int(name):
            print('Please try again')
    except Exception as other:
        print('Something else broke:', other)



