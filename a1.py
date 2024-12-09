#LABS
completed_labs = int(input("Enter the number of labs completed: "))
#completed_labs_weight = 0.2
if completed_labs >= 6:
 labs_points = 20
else:
 labs_points =round((completed_labs/6*20), 2) 


#QUIZZES
completed_quizzes = int(input("Enter the number of quizzes completed: "))
#completed_quizzes_weight=0.15
if completed_quizzes >= 6:
 quizzes_points = 15
else:
 quizzes_points = round((completed_quizzes/6*15), 2)



#ASSIGNMENT 1
Assignment_1= int(input("Enter grade for Assignment 1: "))
assignment_1_weight=0.04
a1_points = round(Assignment_1 * assignment_1_weight, 2)



#ASSIGNMENT 2
Assignment_2=int(input("Enter grade for Assignment 2: "))
assignment_2_weight=0.04
a2_points = round(Assignment_2 * assignment_2_weight, 2)



#ASSIGNEMNT 3
Assignment_3=int(input("Enter grade for Assignment 3: "))
assignment_3_weight=0.04
a3_points =round(Assignment_3 * assignment_3_weight, 2)



#ASSIGNMENT 4
Assignment_4 =int(input("Enter grade for Assignment 4: "))
assignment_4_weight=0.04
a4_ponits = round(Assignment_4 * assignment_4_weight, 2)



#MIDTERM 1
midterm_1= int(input("Enter grade for Midterm 1: "))
midterm_1_weight = 0.125
m1_points = round(midterm_1 * midterm_1_weight, 2)



#MIDTERM 2
midterm_2=int(input("Enter grade for Midterm 2: "))
midterm_2_weight = 0.125
m2_points = round(midterm_2 * midterm_2_weight, 2)



#FINAL EXAM
Final_exam =int(input("Enter grade for Final Exam: "))
Final_exam_weight = 0.18
final_points = round(Final_exam * Final_exam_weight, 2)



#PREPARATIONS
Preparation = int(input("Enter grade for Midterms and Final Preparation: "))
Preparation_weight = 0.06
preparation_points = round(Preparation * Preparation_weight, 2)



#FINAL GRADE
final_grade = labs_points +  quizzes_points + a1_points + a2_points + a3_points + a4_ponits+ m1_points + m2_points + final_points + preparation_points

print("Your final grade is" + str(final_grade))


#PASS OR FAIL 
if final_grade >= 60:
  print( "YOU PASSED YAYYY")
else:
  print( "YOU FALILED MahaHAHA, better luck next time ;)")
