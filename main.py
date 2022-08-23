# # # # # # print("Please enter your the number of students")
# # # # # # numberofstudents = int(input())
# # # # # #
# # # # # # namesofstudents = []
# # # # # # i = 0
# # # # # # while i <numberofstudents:
# # # # # #     print("Enter the name of students number ==>"+ str(i))
# # # # # #     y = input()
# # # # # #     namesofstudents.append(y)
# # # # # #     i+=1
# # # # # #
# # # # # # print("This is what you input ")
# # # # # # z=0
# # # # # # while z < len(namesofstudents):
# # # # # #     print(str(z)+": "+(namesofstudents[z]))
# # # # # #     z+=1
# # # # # #
# # # # # #
# # # # # # #CUMULATIVE STARTS HERE=====================================================================HERE===========================================
# # # # # #
# # # # # # #===============================================================HERE======================================================================
# # # # # #
# # # # # # print("Please enter number of students")
# # # # # # studentsnumber=int(input())
# # # # # #
# # # # # # studentmarks=[]
# # # # # # # j=0
# # # # # # # while j<studentsnumber :
# # # # # # #     print("Please enter student marks for student number "+ str(j))
# # # # # # #     marksofsinglestudent=int(input())
# # # # # # #     if j==0:
# # # # # # #         studentmarks.append(marksofsinglestudent)
# # # # # # #         j+=1
# # # # # # #         continue
# # # # # # #     cumulative_sum=studentmarks[j-1]+marksofsinglestudent
# # # # # # #     studentmarks.append(cumulative_sum)
# # # # # # #     print("==========Cumulative as at index:"+str(j)+"   is==========>"+str(cumulative_sum))
# # # # # # #     j+=1
# # # # # # #
# # # # # # # #CUMULATIVE SUM ENDS HERE
# # # # # # #
# # # # # # i = 1
# # # # # # while i < 6:
# # # # # #     print(i)
# # # # # #     if (i == 3):
# # # # # #       break
# # # # # #     i += 1
# # # # # # i = 0
# # # # # # while i < 6:
# # # # # #   i += 1
# # # # # #   if i == 3:
# # # # # #     continue
# # # # # #   print(i)
# # # # # #
# # # # # # speech = "She said: \"Hi\""
# # # # # # print(speech)
# # # # # # days = 365
# # # # # # print(f"There are {days} in a year")
# # # # # # def my_function():
# # # # #
# # # # # # print("Hello")
# # # # # # name = input("What is Your name:")
# # # # # # print("Pleased to meet you" + name)
# # # # # # location = input("Where do you come from my guy:")
# # # # # # print(location + "! I hear that is a good place to visit")
# # # # # # print("95637+12")
# # # # # # score = 67
# # # # # # if score < 80 and score > 70:
# # # # # #     print("A")
# # # # # # elif score < 90 or score > 80:
# # # # # #     print("B")
# # # # # # elif score > 60:
# # # # # #     print("C")
# # # # # # else:
# # # # # #     print("D")
# # # # #
# # # # # # def a_function(a_parameter):
# # # # # #     a_variable = 15
# # # # # #     return a_parameter
# # # # # # a_function(10)
# # # # # # print(a_variable)
# # # # #
# # # # # # def outer_function(a, b):
# # # # # #     def inner_function(c, d):
# # # # # #         return c + d
# # # # # #     return inner_function(a, b)
# # # # # #
# # # # # # result = outer_function(5, 10)
# # # # # # print(result)
# # # # # # def foo(a, b=4, c=6):
# # # # # #     print(a, b, c)
# # # # # #
# # # # # # foo(20, c=12)
# # # # # # def all_aboard(a, *args, **kw):
# # # # # #     print(a, args, kw)
# # # # # #
# # # # # # all_aboard(4, 7, 3, 0, x=10, y=64)
# # # # # # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # # # # result = [num + 3 for num in numbers if num % 2 == 0]
# # # # # # print(result)
# # # # # # friends = ["Allan","Caleb","Cyril"]
# # # # # # for friend in friends:
# # # # # #     print(friend)
# # # # # #     print(friend + " Mtumishi")
# # # # # student_heights = input("Input a list of student heights").split(",")
# # # # # for n in range(0, len(student_heights)):
# # # # #     student_heights[n] = int(student_heights[n])
# # # # # print(student_heights)
# # # # # # total_height = sum(student_heights)
# # # # # total_height = 0
# # # # # for height in student_heights:
# # # # #     # total_height = total_height + height
# # # # #     total_height += height
# # # # # print(total_height)
# # # # #
# # # # # number_of_students = 0
# # # # # for student in student_heights:
# # # # #     number_of_students += 1
# # # # # print(number_of_students)
# # # # #
# # # # # average_height = round(total_height/number_of_students)
# # # # # print(average_height)
# # # # # student_scores = input("Input a list of student scores ").split(",")
# # # # # for n in range(0, len(student_scores)):
# # # # #     student_scores[n] = int(student_scores[n])
# # # # # print(student_scores)
# # # # #
# # # # # highest_score = 0
# # # # # for score in student_scores:
# # # # #     if score > highest_score:
# # # # #         highest_score = score
# # # # # print(f"The highest score in the class is {highest_score}")
# # # # i = 0
# # # # while i < 101:
# # # #      print(str(i) + ': BK')
# # # #      i += 1
# # # print("Please enter the number of items you need")
# # # numbers_of_items = int(input())
# # # i = 0
# # # fruits_zangu = []
# # # while i < numbers_of_items:
# # #       tundalako = print("Enter item number {0}".format(str(i)))
# # #       fruits_zangu.append(tundalako)
# # #       i += 1
# # i = 0
# # print("Please input the number of items you want")
# # number_of_items = int(input())
# # my_list_of_items = []
# # while i <= number_of_items:
# #     my_list_of_items.append(i)
# #     i += 1
# # print("This is your list: " + str(my_list_of_items))
# #
# # print("How many items do you want to remove from the list")
# # remove_items = int(input())
# # k = 0
# #
# # while k <= remove_items:
# #     j = int(input("enter item number  " + " " + str(k)))
# #     my_list_of_items.remove(j)
# #     k += 1
# #
# # # printing a list one by one
# # m = 0  # beginning of the point
# # h = (len(my_list_of_items)-1)  # the last item
# #
# # while m <= h:
# #     print(my_list_of_items[m])
# #     m += 1
# # print("Please enter number of items")
# # number_of_items =int(input())
# # list_of_items =[]
# # i = 0
# # while i <number_of_items:
# #     print("Please at that index" + str(i))
# #     item = int(input())
# #     #Condition to ignore values that are at index 0 starts here
# #     if i == 0:
# #         list_of_items.append(item)
# #         i+=1
# #         continue
# #     #The condition ends here
# #     j = list_of_items[i-1] + item
# #     list_of_items.append(j)
# #     print(j)
# #     i+=1
# # removing the fruits
# # print("Please enter the number of fruits you need to add")
# # number_of_fruits = int(input())
# # list_of_fruits = []
# # k = 0
# # while k < number_of_fruits:
# #     print("Please print fruit name" + str(k))
# #     fruit = input()
# #     list_of_fruits.append(fruit)
# #     k += 1
# #
# # print("Please indicate items you would like to remove" + str(m))
# # m = 0
# # while m < number_of_fruits:
# #
# #     m = list_of_fruits[i-1]
# #     list_of_fruits.remove(m)
# #     m += 1
#
# # ageyako = int(input("Please input your age"))
# # if ageyako > 18:
# #   print("umetosha mboga")
# # else:
# #   print("bado hujatosha mboga")
# # prompts user to input no. of students, their individual ages, in a list/ range, gives a list of underage students
# number_of_students = int(input("Please input the number of you would like to add: "))
# list_of_student_age = []
# start_point = 0
# for start_point in range(number_of_students):
#     individual_student_age = int(input("Enter the individual student age" + str(start_point) + ":"))
#     list_of_student_age.append(individual_student_age)
# print("This is your age list:" + str(list_of_student_age))
#
# # for start_point in list_of_student_age:
# #     if start_point < 18:
# #         print  ("Under age student : " + str(start_point))
# #     else:
# #         print("Suitable student age : " + str(start_point))
# list_items = []
# for start_point in list_of_student_age:
#     if start_point < 18:
#         list_items.append(start_point)
#     else:
#         print("Above 18 students:" + str(list_of_student_age))
#
# for i in list_items:
# #     list_of_student_age.remove(i)
# # print(list_of_student_age)
#
# # Define a function
# # def addTwoNumbers(a, b):
# #     c = a + b
# #     print(c)
# #
# #
# # # Calling function
# # addTwoNumbers(23, 17)
#
# # Write a function that takes in an array and sums all the arguments
# # def suminarray()
# # def print_my_name(c):
# #
# #      print(c)
# # c = input("nIAJE UNAITwa?")
# # print_my_name(c)
#
# # def salary_tax(a,b,c, d, e):
# #
# #     tax_cap = a * b * c * d * e
# #     print(tax_cap)
# # salary_tax(25000, 0.03, 0.01, 0.03, 0.25)
#
# # def summation_function(addition_argument):
# #     total = 0
# #     for i in addition_argument:
# #         total += i
# #     print(total)
# #
# # addition_argument =[2,4,5,6]
# #
# #
# # summation_function(addition_argument)
#
# # number_of_items = int(input("Add the number of items you will add in the list: "))
# # listofitems = []
# # start_point = 0
# # while start_point < number_of_items:
# #     individual_items = int(input("Please add individual list of items " + str(start_point) + ": "))
# #     listofitems.append(individual_items)
# #     start_point += 1
# # # print(listofitems)
# #
# # def summation_function(f):
# #     total = 0
# #     for i in f:
# #      total = i*i
# #     print(total)
#
# # summation_function(listofitems)
# class Student:
#     def __init__(self, first_name, second_name, age):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.age = age
#
#     def add_age(self):
#         return self.age + 30
#
#     def concatenate(self):
#         return self.first_name + " " + self.second_name
#
#     def last_name(self):
#         return self.second_name
#
#
# number_of_students = int(input("Input number of students: "))
# i = 0
# list_of_students = []
# while i < number_of_students:
#     individual_student = input("Please input firstname, secondname, age: ").split(",")
#     individual_student = Student(individual_student[0], individual_student[1], individual_student[2])
#     list_of_students.append(individual_student)
#     i += 1
#
# # point i in range x (integers, longs, float, )- limit : every is an item in the range
# # i gives you access to properties of list, represent any object in a list = bkay(i.food)
# for i in list_of_students:
#     print(i.second_name)
#
#
# def add_age(student_list):
#     total = 0
#     for student in student_list:
#         total += int(student.age)
#     return total
#
#
# print(add_age(list_of_students))


# BKay = Student("Bkay","Uji", 40)
# Caleb = Student("Caleb", "Chapo", 70)
# print(BKay.add_age())
# print(Caleb.add_age())
# print(BKay.concatenate())
# list_of_students = []
# list_of_students.append(BKay)
# list_of_students.append(Caleb)
# for i in list_of_students:
#     print(i.last_name())
class University:
    def __init__(self, school):
        self.school = school


class School:
    def __init__(self, school_name, faculty):
        self.school_name = school_name
        self.faculty = faculty

class Faculties:
    def __init__(self, faculty_name, department):
        self.faculty_name = faculty_name
        self.department = department


class Department:
    def __init__(self, department_name, students):
        self.department_name = department_name
        self.students = students


class Students:
    def __init__(self, first_name, second_name, course_of_study, year_group):
        self.first_name = first_name
        self.second_name = second_name
        self.course_of_study = course_of_study
        self.year_group = year_group

    def full_details(self):
        return self.first_name + " " + self.second_name + " " + self.course_of_study + " " + self.year_group


def getStudents():
    number_of_students = int(input("Please input number of students: "))
    list_of_students = []
    j = 0
    while j < number_of_students:
        individual_student = input("Please input first_name, second_name, course_of_study, year_group: ").split(",")
        individual_student = Students(individual_student[0], individual_student[1], individual_student[2],
                                      individual_student[3])
        list_of_students.append(individual_student)
        j += 1
    return list_of_students


def getDepartment():
    number_of_departments = int(input("Input number of departments: "))
    i = 0
    list_of_departments = []
    while i < number_of_departments:
        individual_department_name = input("Please add individual name of department " + str(i) + ": ")
        students_under_department = getStudents()
        individual_department = Department(individual_department_name, students_under_department)
        list_of_departments.append(individual_department)
        i += 1
    return list_of_departments


def getFaculties():
    number_of_faculties = int(input("Input number of faculties: "))
    i = 0
    list_of_faculties = []
    while i < number_of_faculties:
        individual_faculty_name = input("Please add individual name of faculty " + str(i) + ": ")
        department_under_faculty = getDepartment()
        individual_faculty = School(individual_faculty_name, department_under_faculty)
        list_of_faculties.append(individual_faculty)
        i += 1
    return list_of_faculties


def getSchool():
    number_of_schools = int(input("Please Input number of schools: "))
    i = 0
    list_of_schools = []
    while i < number_of_schools:
        individual_school_name = input("Please add individual name of school " + str(i) + ": ")
        faculties_under_school = getFaculties()
        individual_school = School(individual_school_name, faculties_under_school)
        list_of_schools.append(individual_school)
        i += 1
    return list_of_schools


print("Welcome to Elimu System. Please input the name of your university")
universityname = input("Name:")
print("Welcome" + universityname)
print("You are successfully logged in:")
y = getSchool()
w = getFaculties()
x = getDepartment()
z = getStudents()


for i in x:
    print("===========" + i.school_name + "===============" + i.faculty_name+ "===============" + i.department_name + "===================")
    for z in i.students:
        print(z.full_details())
    print("==============END===================")
