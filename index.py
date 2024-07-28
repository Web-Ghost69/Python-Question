#  1- Write a program to check if  a number is positive:

num=int(input("Enter the number"))
if num>0:
 print("Number is positive")
else:
 print("Number is negative")




#2-Write a program if number is odd or even:
num=int(input("Enter the number"))

if num%2==0:
    print("Number is even")
else:
    print("number is odd")


# 3-Write a program check whether the passed letter is a vowel or not

Letter= input("Enter the letter:")
if(Letter in "aeiou") or (Letter in "AEIOU"):
    print("Is is vowel")
else:
    print("It is not a vowel")


# 4- Write a program to check if the number is 1 digt ,2 digit,3, digit or 4 digit 

num=int(input("Enter the number"))

if(num>0 and num<=9):
    print("it is 1 digit number")
elif(num>=10 and num<=99):
    print("It is 2 digit")
elif(num>=100 and num<=999):
    print("It is 3 digit")
elif(num>=1000 and num<=9999):
    print("It is 4 digit")
else:
    print("Invalid number")





 

