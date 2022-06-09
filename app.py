##printing triangle


print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /____ |")

##variables

character_name ="bethwel musin"
character_age = "23"

print("Iam "+ character_name +"  from kenya and iam "+ character_age +" years old ")



##strings

phrase ="python programming language"

print(phrase + " is cool")## concatination
print(phrase [9] ) ##printing specific char in the string , 
print(phrase.upper())
print(phrase.replace("python", "javascript"))


##taking input from users and stoeing them
name = input("Enter your name:")
title = input("Enter your title:")

print("Hello " + name+ "!"  "you are a " +title)


## a basic calculator



num1= float(input("Enter the first number:"))
op = input("Enter operator: " )
num2= float(input("Enter the second number:"))

if op == "+":
  print(num1 + num2)

if op == "-":
  print(num1 - num2)

if op == "+":
  print(num1 * num2)

if op == "+":
  print(num1 / num2)
else:
    print("invalid operator")



# result = float(num1)+ float(num2)

# print(result)

##madlips game
color =input(" Enter your favourite color: ")
noun =input(" Enter your favourite noun: ")
celebrity =input(" Enter your favourite celebrity: ")


print("Roses are " +color)
print( noun +  " is blue")
print("Ilove you " +celebrity)


## lists

friends= ['mavo', 'clinton','valarie']#array
for friend in friends:
    print(friend)
friends.append("coder")#add
friends.pop()#remove
friends.insert(1,"coder")#insert a string in the list at specific index

print(friends)

##functions

def sayhi(name):

 print("hello " + name )

sayhi("mike")



# returning functions

def cube(num):
  return num*num*num
result =cube(4)

print(result)

#if statement

is_developer =True
is_jsguru: False
if is_developer or is_jsguru:
   print("you are a developer or fullstack dev or both")
else:
    print("you are a joker")

#dictionaries

weekday ={
"mon":"monday",
"Tue":"Tuesday",
"wed" :"wednesday",
"Thur":"Thursday",
}

print(weekday.get ("mon") )

##while loop
j = 0
while j<=10:
    print(j)
    j +=1

# print("the end")    

i=1
while i<= 10:
    print(i)
    i +=1

 ## Write a program to print first 10 integers and their squares using while loop. 

num = 1
print("Numbers\t\tSquares")
while(num<=10):
   print(num,"\t\t\t\t", num ** 2)
   num = num + 1

##Write a program to find the sum of all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.
num1 = int(input("Enter first number  : "))
num2 = int(input("Enter second number  : "))
if num1 > num2:
   while(num1>num2):
     if num2 % 2 == 0:
       print(num2)
     num2 = num2 + 1
else:
   while(num1<num2):
     if num1 % 2 == 0:
       print(num1)
     num1 = num1 + 1

##Write a program to print first 10 natural number in reverse order using while loop.
num = 10
while num >= 1:
     print(num)
     num= num - 1


#Write a program to print sum of first 10 Natural numbers.

num = 10
sum = 0
while num >= 1:
   sum = sum + num
   num= num - 1
print(sum)

#Write a program to check whether a number is prime or not using while loop.
num1 = int(input("Enter any number : "))
k=0
if num1 == 0 or num1 == 1:
    print("Not a prime number ")
else:
   i = 2
   while(i<num1):
     if num1 % i == 0:
       k = k+1
     i = i+1
if k == 0 :
        print( num1,"is prime number")
else:
        print(num1, "is not prime number")

 
