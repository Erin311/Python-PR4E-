score = raw_input("Enter a score: ")

def gradef(score):
    if score > 1  or score < 0:
        score = 'None'
    elif score >= 0.9 :
        grade = 'A'
    elif score >= 0.8 :
        grade = 'B'
    elif score >= 0.7 :
        grade = 'C'
    elif score >=0.6 :
        grade = 'D'
    else :
        grade = 'F'
    return grade
    
try:
    score = float(score)
    print gradef(score)
except:
    print "Error please enter only numbers!"