inp = input('Enter score:')

score = float(inp)

def computeGrade(score):
    if score <= 0.0 and score >= 1.0 :
        print('ERROR')
        return score
    else :
        if score >= 0.9 :
            print('A')
            return score
        elif score >= 0.8 and score < 0.9:
            print('B')
            return score
        elif score >= 0.7 and score < 0.8:
            print('c')
            return score
        elif score >= 0.6 and score < 0.7:
            print('D')
            return score
        elif score < 0.6 :
            print('F')
            return score

grade = computeGrade(score)
print(grade)