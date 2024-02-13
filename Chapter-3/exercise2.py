inp = input('Enter Hours :')
inp1 = input('Enter Rate :')

try :
    hour = float(inp)
    rate = float(inp1)
    pay = hour * rate
    print(pay)
except :
    print('Please Enter numeric input:')