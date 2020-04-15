while True:
    value = input("enter, for exit 'q':")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        print(number, 'squared is', number * number)
    else:
        continue

guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('tow low')
    elif start == guess_me:
        print('found it')
        break
    elif start > guess_me:
        print('oops')
        break
    start += 1


for a in range(4, -1, -1):
    print(a)

list = [3, 2, 1, 0]
for x in list:
    print(x)

list2 = [x for x in range(0, 11) if x % 2 == 1]

squares = {a: a*a for a in range(11)}

odd={z for z in range(11) if z % 2 == 0}

for some in ('Got %s' % z for z in range(11)):
    print(some)

def good():
    return ['Harry', 'Ron', 'Hermione']


def get_odds():
    for z in range(1,10,2):
        yield z
for count, z in enumerate(get_odds(), 1):
    if count==3:
        print('this is third number', z)
        break

def test(func):
    def new(*args):
        print('start')
        result = func(*args)
        print(result)
        print('end')
    return new
@test
def add(a, b):
    return a + b

class OopsException(Exception):
    pass

names = ['Klara', 'Tom', 'Ron', 'sara']
for name in names:
    if name.islower():
        raise OopsException(name)

while True:
    stroka = input('Enter here name with big first letter [q for exit:]')
    if stroka == 'q':
        break
    try:
        for name in names:
            if stroka == name.capitalize():
                print('You are diligent boy:', name)
    except OopsException as err:
        if stroka == int():
            print('Caught an oops, only with big letter:', name)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
