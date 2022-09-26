# a = int(input("Please input the value of a"))
# b = int(input("Please input the value of b"))
# c = int(input("Please input the value of the gradient"))
#
# x = int(input("Please input the value of x "))
#
#     def last_name(self):
#         return self.second_name
#
# for y in "Caleb":
#     print(y)

# x = input("Enter name to be reversed")
# name = x
# print(name)
#
# print(x[::-1])


# bk_data_analyst_tools = ['Excel', 'python', 'SQL', 'R', 'power Bi', 'Tableau']
# print(type(bk_data_analyst_tools))
# print(bk_data_analyst_tools[-4:-1])

# checking if an item exists in a list
# if "R" in bk_data_analyst_tools:
#     print("Yes R is a tool BKay uses for data analytics")

# Changing Item value
# bk_data_analyst_tools[-1] = "Looker"
# print(bk_data_analyst_tools)
#
# # Changing a Range Of Item Values
# bk_data_analyst_tools[-1:-3] = ["Tableau", "Google Data Studio"]
# print(bk_data_analyst_tools)
#
# bk_data_analyst_tools[1:3] = ["Access"]
# print(bk_data_analyst_tools)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert method() method.
# The insert () method inserts an item at the specified index:
# list.insert(index, item)

# bk_data_analyst_tools.insert(2, "SQL")
# print(bk_data_analyst_tools)

# ADD LIST ITEMS
# Append Items
# To add an item to the end of the list, use the append() method:
# bk_data_analyst_tools.append("PostgreSql")
# print(bk_data_analyst_tools)
#
# bk_data_analyst_mind = ["Analytical", "problem Solving", "Critical Thinking"]
# bk_data_analyst_mind.extend(bk_data_analyst_tools)

# Add Any Iterable
# bk_data_tuple = ("resilience", "commitment", "consistency")
# bk_data_analyst_tools.extend(bk_data_tuple)
# print(bk_data_analyst_tools)
# bk_data_analyst_tools.remove("PostgreSql")
# print(bk_data_analyst_tools)

# Remove Specified Item you use Pop()
# If I don't specify pop() remove the last item
# bk_data_analyst_tools.pop(1)
# print(bk_data_analyst_tools)
# bk_data_analyst_tools.pop()
# print(bk_data_analyst_tools)

# The del keyword removes a specified index
# del bk_data_analyst_tools[5:7]
# print(bk_data_analyst_tools)

# del bk_data_analyst_mind  # deletes the whole list

# Clear the List
# clear() - Empties the list become empty


# Loop Lists
# Loop Through a List
# Print all items in the list, one by one
# for x in bk_data_analyst_tools:
#     print(x)

# # Loop through the Index Numbers
# # I can loop through the list of items by reffering to their index number.
# # use the range() and len() functions to create a suitable iterable.
# for i in range(len(bk_data_analyst_tools)):
#     print(bk_data_analyst_tools[i])

# Using a While Loop
# i = 0
# while i < len(bk_data_analyst_tools):
#     print(bk_data_analyst_tools[i])
#     i = i + 1
#
# # Looping Using List Comprehension
# [print(x) for x in bk_data_analyst_tools]

# LIST COMPREHENSION
#  offers a shorter syntax when you want to create a new list based on the values of an existing list
# important_tools = []
#
# for x in bk_data_analyst_tools:
#     if "P" in x:
#         important_tools.append(x)
#
# print(important_tools)
#
# important_tools = [x for x in bk_data_analyst_tools if "i" in x]
# print(important_tools)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# The condition is like a filter that only accepts the items that valuate to True
# newlist = [x for x in bk_data_analyst_tools if x != "Resilience"]
# print(newlist)
# newer_list = [i for i in bk_data_analyst_tools]
# print(newer_list)
#
# # Iterable
# # The iterable can be any iterable object, list, tuple, set etc
# b = [x for x in range(10)]
# print(b)
#
# respect = [x.upper() for x in bk_data_analyst_tools]
# print(respect)
#
# greetings = ['Muhimu Sana' for x in bk_data_analyst_tools]
# print(greetings)
#
# newest_list = [x if x != "Resilience" else "Talent" for x in bk_data_analyst_tools]
# print(newest_list)
#
# bk_data_analyst_tools.sort()
# print(bk_data_analyst_tools)
#
# # sort Numerically
# numba: list[int] = [100, 50, 65, 82, 23]
# numba.sort()
# print(numba)


# numba.sort(reverse= True)
# print(numba)


# Customize Sort Function
# def myfunc(n):
#     return abs(n - 50)
#
#
# numba = [100, 50, 65, 82, 23]
# numba.sort(key = myfunc)
# print(numba)
#
#
# bk_data_analyst_tools.sort()
# print(bk_data_analyst_tools)
# bk_data_analyst_tools.sort(key = str.lower)
# print(bk_data_analyst_tools)
#
# # bk_data_analyst_tools.reverse()
# # print(bk_data_analyst_tools)
#
#
# # Copy Lists - using copy() method
# bk_infrastructure = bk_data_analyst_tools.copy()
# print(bk_infrastructure)
#
# # Copy Lists - using list() method
# bk_intel = list(bk_data_analyst_mind)
# print(bk_intel)

# Join Two Lists
# Several ways are available to join, concatenate, two or more lists in Python
# Using the + operator
# bk_person = bk_data_analyst_tools + bk_data_analyst_mind
# print(bk_person)
#
# list1 = ["A", "B", "C"]
# list2 = [1, 2, 3]
#
# for x in list2:
#     list1.append(x)
#
# print(list1)
#
# list1 = ["A", "B", "C", "D", "E"]
# list2 = [1, 2, 3, 4, 5]
# list1.extend(list2)
# print(list1)

# List append() Method
# append() method appends an element to the end of the list
# Syntax => list.append(elmnt: required. An element of any type(string, number, object etc))


# analytics_tools = ['Excel', 'SQL', 'Python', 'R']
# visualization_tools = ['Power Bi', 'Tableau', 'Looker', 'Google Data Studio']
# analytics_tools.extend(visualization_tools)
# print(analytics_tools)
#
# fruits = ['a', 'b','c','c', 'd']
# x = fruits.count('b')
# print(x)
# fruits.clear()
# copy => list.copy()
# alphabet = fruits.copy()

# count() => returns the number of elements with the specified value
# list.count(value: required. Any type; number, list, tuple,etc.) The value to search for.

#
# # extend() : adds specified list elements (or any iterable) to the end of the current list.
# fruits = ['a', 'b', 'c', 's']
# points = (1, 2, 3, 8, 9)
# fruits.extend(points)
# print(fruits)
#
#
# # Index() Method: the index() returns the position at the first occurence of the specified value
# # list.index(elmnt)
# x =fruits.index('a')
# print(x)
#
# # Insert => list.insert(pos, elmnt)
# fruits.insert(3, 'd')
# print(fruits)
#
#
# # Pop() removes the element at the specified position
# fruits.pop(3)
# fruits.remove('b')
# print(fruits)
# i = 1
# while i < 6:
#   i += 1
#   if i == 3:
#       continue
#   print(i)
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# A for loop is used for iterating over a sequence.
# With the for loop we can execute a set of statements once for each item in a list, tuple, set, etc
# fruits = ["apple", "banana", "cherry"]
# for b in fruits:
#     print(b)
#
# for v in "boniface":
#     print(v)
#
# fruits = ["apple", "banana", "cherry"]
# for b in fruits:
#     print(b)
#     if b == "banana":
#         break

# the continue Statement
# with the continue statement we can stop the current iteration of the loop, and continue with the next:
# fruits = ['a', 'b', 'c', 'd', 'e']
# for x in fruits:
#     if x == 'c':
#         continue
#     print(x)


# The range Function
# to loop through a set of code a specified number of times, we can use the range() function
# The range(0 function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# for x in range(6):
#     print(x)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# for c in range (2, 30, 3):
#     print(x)
#
# #else in loop
# # print all numbers from 0-5 and print when the loop has ended
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished")
# the else block will not be executed if the loop is stopped by a break statement
# for x in range(6):
#     if x == 3: break
#     print(x)
# else:
#     print("Finally kameisha")
# Nested Loops: A loop inside a loop. the inner loop will be esecuted for each iteration of the outer loop
# mindset = ['Data visualization', 'Data collection', 'Data Preparation', 'Data Analysis', 'Data Storytelling']
# tools = ['Power Bi', 'Google Forms', 'Excel', 'Python', 'Power Point']
# for x in mindset:
#     for y in tools:
#         print(x, y)

# The pass statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid an error
# for x in [0, 1, 2]:
#     pass

# break mean exit
# continue means jump to the next item

# Function.
# A function is a block of code that runs when it is called.
# You can pass data known as parameters, into a function
# A fxn can return data as a result
# CREATING A FXN
# In python a fxn is defined using a def keyword:
# def my_fxn():
#     print('Hello BKay')
# # CALLING A FUNCTION
# # To call a fxn, use the fxn name followed by parenthesis
#
#
# my_fxn()
# ARGUMENTS
# Information can be passed into functions as arguments.
# Arguments are specified after the fxn name, inside the parenthesis. You can add as many arguments as you want, just separate by comma.
# The following example ahas ana example with one argument (fname). When the fxn is called, we pass along a first name, which is used inside the fxn to print the fullname
# def my_fxn(fname: object) -> object:
#     print(fname + " Kuria")
#
#
# my_fxn("Boniface")
# my_fxn('Ngigi')
# my_fxn('Kamara')
# Arguments are often shortened to args.
# PARAMETERS OR ARGUMENTS?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# suffer less(daughter, brother, mother, BKay, church)

x = "awesome"

"""def myfunc():
	global x
	x = "fantastic"
	print("Python is " + x)


myfunc()

print("Python is " + x)

# x = 1j
# print(type(x))

x = 35e3
y = 12E4
z = -87.7e100

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
def greeting(name, department):
	print("Welcome, " + name)
	print("You are part of " + department)


greeting("BK", "Statistics")

def print_seconds(hours, minutes, seconds):
	print((hours*60*60) + (minutes*60) + seconds)



print_seconds(1,2,3)


def area_triangle(base, height):
	return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = (area_b + area_a)
print("The sum of both areas is: " + str(sum))

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours * 3600) // 60
	remaining_seconds = seconds - hours * 3600 - minutes * 60
	return  hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

We use the return keyword in a function, which tells the function to pass data back.
When we call the function, we can store the returned value in a variable.
Return values allow our functions to be more flexible and powerful, so they can be used reused and called multiple times.

functions can even return multiple values. Don't forget to store all returned values in variables. 
You could also have a function nothing, in which the functions simply exists.




name = input("Please input your name: ")
number = len(name) * 9

print("hello " + name + ". Your lucky number is " + str(number))

name = input("Please input your name: ")
name2 = list(name)
len_of_name = len(name)
x = 0

while x <= len_of_name:
	name2 = name2[x:len_of_name]
	len_of_name = len_of_name -1
	print(name2)


def lucky_number(name):
	number = len(name)*9
	print("Hello " + name + ". Your lucky number is: " + str(number))

lucky_number(input("Please input your name"))

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")


def days_of_month(month, days):
	print(month + "has " + str(days) + " days.")

days_of_month("June ", 30)
days_of_month("July ", 31)

Self-documenting code: written in a way that's readable and doesn't conceal its intent


def rectangle_area(base, height):
	calculate_area = base * height
	print("The area is " + str(calculate_area))

rectangle_area(5, 6)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km 

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))

def lucky_number(name):
  number = len(name) * 9
  name = "Hello " + name + ". Your lucky number is " + str(number)
  return name
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller, bigger)

my_list = [3, 1, 1]
my_list[-1] = my_list[-2]
print(my_list)

my_list = [0,1,2,3]
x = 1
for elem in my_list:
    x *= elem
print(x)

i = 2
while i >= 0:
    print("*")
    i -= 2

for i in range (-1, 1):
    print('#')

z = 10
y = 0
x = z > y or z == y
print(x)

vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
print(vals)
my_list3 = [0 for i in range (1,3)]
print(my_list3)

print(2**2**3)

x = int(input("Please in how many items you want named: "))
z = []


def my_func():
    for i in range(x):
        y = input(("Please enter a name for item " + str(i) + ": "))
        z.append(y)


my_func()
print(z)



def sumstuff(a, b):
    print(a + b)


sumstuff(4, 6)

for x in "banana":
  print(x)
  
A function is a block of code which only runs when it is called.
You can pass data known as parameters into a function
A function can return data as a result
Information can be passed into functions as arguments.
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
def my_function() -> object:
    print("Hello from a function")


my_function()

def my_function(fname, lname):
  print((fname + " " + lname))

my_function("BK", "Kamara")


def my_function(*kids):
  print("My initials are" + kids[1])

my_function(" B"," K"," N")

def my_function(child1, child2, child3):
  print("The youngest is "+ child3)


my_function(child1= "A", child2="B", child3="C")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass


1wwwtrykl

!def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


my = "one_two!three_four"
my2  = my.replace('_', '!')
print(my2)

a = [2, 3, 5, 7]
# print(sum(a))
b = [1, 4, 7, 8]



def mysum(a):
    total = 0
    for i in range(0, len(a)):
        total = total + a[i]
        return total


mysum(a)
print(mysum(a))


class MyDelimiter:
    def __init__(self, name1, delimiter):
        self.name1 = name1
        self.delimiter = delimiter


    def remove_my_delimiter(self):
        print('This is my email without' +str( self.name1.split("@")))

Bkay = MyDelimiter("bkkamara2020@gmail.com", "@")
Bkay.remove_my_delimiter()

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[:5])

a = "Hello, World!"
print(a.split(","))
print(a.replace("H", "B"))

FORMAT method
age = 29
txt = "My name is BKay and I am {} years old"
print(txt.format(age))

print(10 < 9)

zimmermann = 50
ruaka = 60
kariobangi = 30
myJourney = "My journey was from Zimmerman was {} and after work I moved from Ruaka using {} and I finally moved to Kariobangi using {}"
print(myJourney.format(zimmermann,ruaka,kariobangi))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "This will \n insert one \\ (backslash)."
print(txt)

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = 200
print(isinstance(x, int))
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry", "booboo"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

dedication ya nzi
for how long will you do something little?
breadcrumbs in programming
for shame
respect yourself

class Country:
    def __init__(country, name, president, counties):
        country.name = name
        country.president = president
        country.counties = counties

class County(Country):
    def __init__(county, name, governor, senator, women_rep, constituencies):
        county.name = name
        county.governor = governor
        county.senator = senator
        county.women_rep = women_rep
        county.constituencies = constituencies

class Constituency:
    def __init__(constituency, name, mp, wards):
        constituency.name = name
        constituency.mp = mp
        constituency.wards = wards

class Ward:
    def __init__(ward, name, mca):
        ward.name = name
        ward.mca = mca


def getward():

def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


print("big" > "small")
print(11 % 5)

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))


def format_name(first_name, last_name):
	# code goes here
	string = 'Name: ' + ', '.join([name for name in [last_name, first_name] if name]) if any([last_name, first_name]) else ''
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

x = 1
sum = 0
while x < 10:
    sum += x  # sum = sum + x
    x += 1  # x = x + 1
print(sum)

product = 1
while x < 10:
    product = product * x
    x += 1
print(product)


def count_down(current):
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")


count_down(3)
"""


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        n = n + 1
        print(n)


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)


def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


def sum_divisors(n):
  sum = 0
# Return the sum of all divisors of n, not including n
  i = 1
  while i < n:
    if n % i == 0:
      sum += i
      i +=1
    else:
      i+=1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))

print(sum_divisors(3))

print(sum_divisors(36))

print(sum_divisors(102))
