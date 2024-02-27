x = open(r"C:\Users\User\Desktop\test.txt")

for line in x :
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:') :
        a = line.find(':')
        y = x[a + 1: ]
        num = float(y)
        print(num)