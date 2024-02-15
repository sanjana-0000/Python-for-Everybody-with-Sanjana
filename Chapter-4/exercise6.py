inp = input('Enter Hours:')
inp1 = input('Enter Rate:')

hours = float(inp)
rate = float(inp1)

extra_hours = hours - 40

def computepay(hours, rate):
    salary = (extra_hours * 1.5 * rate) + (40 * rate)
    return salary

salary = computepay(hours, rate)

print(salary)