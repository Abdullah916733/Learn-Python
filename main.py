# BASIC PRINT

# print('Hello World'),

# a = input("Enter your name:"),
# print("Your Name is",a),

# BASIC PRINT



# BASIC LOOP

# name = 'Abdullah Ansari'

# for character in name:
#     print(character)

# BASIC LOOP




# STRING METHODS

# name = 'Abdullah'

# print(name.upper())

# STRING METHODS




# IF ELSE CONDITIONS 

# num = input("Enter your age: ")

# if(int(num) >= 18):
#     print("You can drive")
# else:
#     print("You can not drive")

# IF ELSE CONDITIONS 




#  MATCH STATEMENT CONDITIONS

# num = int(input('Enter you age: '))

# match num:
#     case _ if num > 18:
#         print('You are more then 18')
#     case _ if num < 18:
#         print('You are lees than 18')
#     case _:
#         print('Your age is',num)

#  MATCH STATEMENT CONDITIONS

 



#   FUNCTIONS 

# def average(a,b):
#  print('Average of a and b plus', (a+b)/2)
 
# average(3,5)

# def average(*nums):
#   sum = 0
#   for i in nums:
#     sum = sum + i
#   print('Average ', sum / len(nums))

# average(5*6)  

# def names(**names):
#     print(names['fname'],names['mname'],names['lname'])

# names(fname='Abdullah',mname='Abdul Vadud',lname='Ansari')

#   FUNCTIONS






#  LIST 

# list = [i for i in range(10) if i%2==0]
# print(list)

#  LIST





# LIST METHODS

# l = [1,2,5,6,9,3]
# l.sort()
# l.index(2)
# l.append(10)

# print(l)


# LIST METHODS    






#  F STRING 

# name = 'Abdullah'
# country = 'India'

# txt = f"Hello! My name is {name} and I am from {country}."

# print(txt)

#  F STRING





#  Recursive 

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(7))

#  Recursive 






#  TRY AND EXCEPTION
  
# a = input("Enter You Number: ")

# print(f"Multiplication of {a} is:")

# try:
#  for i in range(1,11):
#     print(f"{int(a)} X  {i} = {int(a) * i}")
# except Exception as e:
#     print(e)

# print('Error handle successfully!')

#  TRY AND EXCEPTION  








# KBC EXERCISE 

listOFQuestions = [
    ['What is your Name','Abdullah','Ansari','Abdul Rehman','Amrin',1],
    ['What is your favorite Color','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Place','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite T-shirt','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Pen','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Weather','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Design','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Logo','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Pet','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Exercise','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Time','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Cap','Abdullah','Ansari','Abdul Rehman','Amrin',3],
    ['What is your favorite Car','Abdullah','Ansari','Abdul Rehman','Amrin',3],
]

amountPrice = [1000,2000,5000,6000,10000,30000,70000,100000,400000,10000000]

for i in range(len(listOFQuestions)):
    question = listOFQuestions[i]
    print(f"\n\nThis Question for {amountPrice[i]}")
    print(f"Question {1}: {question[0]}")
    print(f" a. {question[1]}    b.{question[2]}")
    print(f" c. {question[3]}    d.{question[4]}")

    answer = int(input("Enter you answer :"))

    if(answer == question[5]):
        print(f"Correct your answer! You win {amountPrice[i]}")
    else:
        print('Your answer is wrong')
        break
     

# KBC EXERCISE 