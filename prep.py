#with open('manya.txt', 'r') as f:
   # contents=f.read()
   # print(contents)


#class Student:
   # def __init__(self,name, roll_no , place, hobby):
       # self.name = name
        #self.roll_no = roll_no
       # self.place = place
       #def display(self):
        #print(f"Name: {self.name} ,Roll No: {self.roll_no} ,Place: {self.place} ,Hobby: {self.hobby}")

#s1 = Student("Manya",7590,"Muzaffarpur","travelling")        
#s1.display()
#s2 = Student("Paroma",1120,"Patna","Journalling")
#s2.display()
#s3 = Student("Mansi",11199,"Aligarh","Sleeping")
#s3.display()


# INHERITANCE
#class Person:
   # def __init__(self,name):
        #self.name = name 
   # def intro(self):
        #print(f"Hello, I am {self.name}")

#class Student(Person):
    #def __init__(self,name,roll_no):
        #super(). __init__(name)  
        #self.roll_no = roll_no
   # def display(self):
       # print(f"Name: {self.name}, Roll No: {self.roll_no}")

#s2 = Student("Meena",123)  
#s2.intro() 
#s2.display()     


#class Animal:
   #def __init__(self,name):
      #self.name = name 
   #def intro(self):
      #print(f"Hello, I am {self.name}")
   #def sleep(self):
      # print(f"{self.name} is sleeping")
   

#class Cat(Animal):
    #def __init__(self,name,age):
        #super(). __init__(name)  
        #self.age=age
    #def meow(self):
        #print(f"{self.name} says meow")

#s2 = Cat("Zoe",6)  
#s2.sleep() 
#s2.meow()     


#class Animal:
   #def __init__(self,name):
      #self.name = name 
   #def intro(self):
      #print(f"Hello, I am {self.name}")
   #def sleep(self):
      # print(f"{self.name} is sleeping")
   
#class Dog(Animal):
    #def __init__(self,name,age):
       # super(). __init__(name)  
        #self.age=age
   # def bark(self):
       # print(f"{self.name} barks ")

#a1=Dog("TOM",7)
#a1.sleep()
#a1.bark()




# STRING OPERATIONS
#vowels = 'aeiouAEIOU'
#count = 0
#for char in string:
    #if char in vowels:
        # count+=1
#print("Number of vowels:", count)


s= input("Enter a string:")
if s == s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
