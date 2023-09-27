student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


score = 0
for i in student_scores:
    if score < i:
        highest_score = i 
    else:
        highest_score = score
    score = highest_score
print(score)



for m in student_scores:
    if score > m:
        lowest_score = m
    else:
        lowest_score = score
    score = lowest_score
print(score)
        
