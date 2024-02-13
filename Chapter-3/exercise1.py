inp1 = input('Enter Hours: ')
inp2 = input('Enter Rate: ')

hour = float(inp1)
rate = float(inp2)

if hour > 40:
    extra_hours = hour - 40
    pay = (extra_hours * 1.5 * rate) + (40 * rate)
    print('Payment: $' + str(pay))
else:
    pay = hour * rate
    print('Payment: $' + str(pay))
