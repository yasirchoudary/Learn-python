"""
bitwise operator
a= 5
b= 9
print (a&b)
print (a|b)
print (a^b)
print (a>>b)
print (a<<b)
print (~a)
"""


"""
my_list = [1, 2, 3, "apple"]
my_list.append(4)
print (my_list) # [1,2,3,apple,4]

my_range = range(1, 5)  # Generates 1, 2, 3, 4
print(list(my_range))

tuuple = (1,3,4,5, "hfhekfh")
print (tuuple)

dictt = {"name": "ali", "age": 18}
print (dictt["age"])

sett= {1,2,3,4,4,5}
sett.add(7)
print (sett)

nonee = None
print (nonee)

tf= True
print(tf)
print (3<2)"""


"""
checkinstring= 'yasir'
print ('yas' in checkinstring)

numbers = [1,23,4,5,6,75,3]
print (23 not in numbers)
"""

"""
dp= ['yasir','asjad','raza']
name= input ("enter the name: ")

if name in dp:
    print (f"{name}is present")
else:
    print ("name isn't present")
    


a1= {"boy":"yasir", "girl": "hafsa"}
print ("boy" in a1)
"""

"""
a= 100
b= 100
x= 200
c= "yasir"
d= "100"
print (a is b)
print (a is c)
print (c is d)
print (a is x)
"""

"""
qualification = input ("do you have qualification for the job")
marks = int(input("enter your marks"))
if (qualification== 'yes' and marks >=70): print ("you have the job")
else : print ("you dont have job, you can get lost")
"""

"""
#escape sequences
print("yasirnas\njhang") 
print("yasirnas\bjhang") #yasirnajhang
print("yasirnas\tjhang") #yasirnas        jhang
print("yasirnas\rjhang") #jhangnas
print("yasirnas\\jhang") #yasirnas\jhang

#raw string
print(R"yasirnas\njhangsadar\ntehsil")
"""

#modules from logics import add, subtract, multiply, divide
# add(2,3)


"""
#dir function 
x = 100
name = "yasir"
print (dir(x))
print(dir(name))
print (name.upper())


def second():
    name = "yasir"  
    print (locals())
second() #to see if any variable present in function
    
print (type(second)) #to see what is the class type i.e. function
print (dir(second)) # to see what are the methods/functions can be applied
"""

#another function of dir is that it can tell what are the other attributes are prsent in other file, it can also tell what are the
#functions can be applied to the attribute
"""
import second
print (dir(second))
print (second.x)
second.father_name()


from second import *
father_name()#we have used __all__ in other file, so we can import only selected variables, we can do this only in this method
"""


# if-else
#(non-zero values are treated as True, and zero/none value as False)
"""
if True: 
    print ("this statment is working cause we have true in the condition")

if True: 
    print("yes")
    print("again")
print ("yes also")


if False:
    print("its not going to print")
    print("same, its also not going to print")
print ("only this would get printed")


num= int(input("enter a number: "))
if num%2==0:
    print ("the number is even")
else: 
    print("the number is odd")


num= int(input("enter a number: "))
if num%2==0:
    print ("the number is even")
    if num>2:
        print("the number is greater than 2")
    else: 
        print("the number is 2")
else: 
    print("the number is odd")

    
# one-line if else    
a= 4
b=3
print("A is greater") if a>b else print ("A isnt greater than B")


#if else-if
num= int(input("enter a number: "))
if num >= 10 and num < 20:
    print ("the number is greater than ten and less than 20")
elif num >= 20 and num < 30:
    print ("the number is in twenties")
elif num >= 30 and num < 40:
    print ("the number is in thirties") 
else:
    print ("the number is less than 10 or greater than 39")
"""



# while loop
"""
i=1
num= int(input("enter a number: "))
while i<=10:
    print (num,'*',i,'=', num*i)
    i+=1
"""
"""
i=4
while i<4:
    print ("yes")
    i+=1
else:
    print ("we exit")

"""