# def find_sum_and_avg_until_done():
#     sum = 0
#     count = 0
#     while True:
#         user_input = input("Enter a number:")

#         if user_input.lower() == "done":
#             return sum, sum/count
#             break
#         else:
#             count = count + 1
#             sum = sum + int(user_input)


# sum, avg = find_sum_and_avg_until_done()

# print(f"SUM:{sum} and AVG:{avg}")
sum = 0
count = 0

while True:
    inp = input('Enter a number:')
    if inp == 'done' :
        avg = sum / count
        print('Sum:', sum)
        print('count:', count)
        print('Average:', avg)
    else :
        try:
            number = float(inp)
            sum = sum + number
            count = count + 1
        except:
            print('ERROR')
        