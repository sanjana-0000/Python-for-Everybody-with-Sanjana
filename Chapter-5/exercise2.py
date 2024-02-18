number = []

def max(number_list):
    maximum = None
    for value in number_list:
        if maximum is None or value > maximum:
            maximum = value
    return maximum


def min(number_list):
    minimum = None
    for value in number_list:
        if minimum is None or value < minimum:
            minimum = value
    return minimum


while True:
    inp = input('Enter a number(Type exit to stop):')
    if inp == 'done':
        print('maximum:', max(number))
        print('minimum:', min(number))
    else:
        try:
            value = int(inp)
            number.append(value)
            print('list:', number)
        except:
            print('ERROR')

