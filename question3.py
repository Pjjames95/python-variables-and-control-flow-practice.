def grade_score(score):
    if score < 60:
        print("F")
    elif 60 <= score <= 69:
        print("D")
    elif 70 <= score <=79:
        print("C")
    elif 80 <= score <= 89:
        print("B")
    else:
        print("A")
score=int(input("Enter your score(0-100):"))
grade_score(score)
