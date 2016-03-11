def whatDoIBuy(car_price, bike_price):
    if car_price < 1200000:
        print('Buy Car')
    elif bike_price > 60000:
        print('Buy Bike')
    else:
        print('Buy Bicycle')

def whatIsa(a):
    if a == 10:
        print('a is 10')
    elif a != 9:
        print('a is not 10 and not 9')
    else:
        print('a is 9')


def printMyDept(dept):
    if dept == 'IDC':
        print('Industrial Design Center')
    elif dept == 'CS':
        print('Computer Science')
    elif dept == 'EE':
        print('Electrical Engineering')
    else:
        print('No idea bro!')


def itsMe(name):
    if len(name) > 2 and len(name) < 10 and name != 'Adele':
        # You can even write this instead
        # 2 < len(name) < 10 and name != 'Adele'
        print('Hi')
    elif name == 'Adele':
        print('Hello')
    elif name[:3] == 'Ada':
        print('Yo')
    else:
        print('Hey')


#