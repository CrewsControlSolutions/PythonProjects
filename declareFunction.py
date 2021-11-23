

mySentence = 'sees the color'

colorList = ['red','gold','orange','turqoise']


def colorFunction(name):
    lst = []
    for i in colorList:
        msg = '{0} {1} {2}'.format(name,mySentence,i)
        lst.append(msg)
    return lst


def getName():
    hasName = False
    while not hasName:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name.')
        elif name == 'John':
            print('John, you shall not pass!')
        else:
            hasName = True
    lis = colorFunction(name)
    for i in lis:
        print(i) 

getName()
