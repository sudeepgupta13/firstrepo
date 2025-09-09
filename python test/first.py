#print("Hello World")

# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("chikku is crying now")
# engine.runAndWait()

# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

import threading
import time

def func(seconds):
    print(f"Thraed ended after {seconds} second")
    time.sleep(seconds)
 #normal code  
time1 = time.perf_counter() 
# func(3)
# func(2) 
# func(1)
# with thread execution
t1 = threading.Thread(target=func, args=(3,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(f"normal code time {time2 - time1} seconds")