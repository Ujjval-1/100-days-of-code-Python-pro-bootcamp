#-------- List Comprehension new_list = [new_item for item in list]

# numbers = [1,4,9,2]
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# name = "Ujjval"
# letters_list = [letter for letter in name]
# print(letters_list)
#
# range_list = [num*2 for num in range(1,5)]
# print(range_list)

# ---------Conditional List Comprehension new_list = [new_item for item in list if test]

# names = ['ujjval','michael','ashwani','vinay','rajeev','nikhil','ishant','manish','Anand','manoj']
# short_names = [name for name in names if len(name)<6]
# long_names = [name.upper() for name in names if len(name)>6]
#
# print(short_names)
# print(long_names)



# ---------Dictionary Comprehension   new_dict = {new_key:new_value for item in list}
#                            new dict = {new_key:new_value for (key,value) in dict.items()}
# Conditional Dictionary Comprehension     new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# import random
# names = ['ujjval','michael','ashwani','vinay','rajeev','nikhil','ishant','manish','Anand','manoj']
# students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
#
# passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
# print(passed_students)


#-----------------------------------------------------
import pandas
student_dict = {
    "student":["Ujjval","Vinay","Michael"],
    "score":[70,56,64]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)
#Loop through a dataframe
for (key,value) in student_df.items():
    print(key)

#loop through rows of dataframe

for index,row in student_df.iterrows():
    print(row.student)
    print(row.score)



