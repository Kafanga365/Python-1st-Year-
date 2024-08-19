coursework_weight = float(input("Enter the weight of the coursework (in percentage): "))
exam_weight = float(input("Enter the weight of the exam (in percentage): "))

coursework_score = float(input("Enter your coursework score: "))
exam_score = float(input("Enter your exam score: "))

# Calculate the weighted scores
weighted_coursework_score = (coursework_weight / 100) * coursework_score
weighted_exam_score = (exam_weight / 100) * exam_score

# Calculate the overall score
overall_score = weighted_coursework_score + weighted_exam_score

# Calculate the minimum passing score
passing_score = 40

# Check if the student has passed or failed
if overall_score >= passing_score:
    print("Congratulations! You have passed the module.")
else:
    print("Sorry, you have failed the module.")

# Calculate the score needed to pass
score_needed_to_pass = passing_score - overall_score

if score_needed_to_pass > 0:
    print("You need an additional score of", score_needed_to_pass, "to pass the module.")
else:
    print("You have already passed the module.")