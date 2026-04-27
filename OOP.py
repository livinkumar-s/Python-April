
# class Bottle:
#     def __init__(self,h,r):
#          self.heigh=h
#          self.radius=r
#          self.status="closed"
    
#     def printVolume(self):
#          print((22/7)*self.radius*self.radius*self.heigh)
    
#     def open(self):
#          self.status="opened"
#     def close(self):
#          self.status="closed"

# b1=Bottle(10,2)

# b1.heigh=30
# b1.volume=120

# b2=Bottle(20,4)

# b2.heigh=30
# b2.volume=120

# print(b1.volume)

# b1.printVolume()
# b2.printVolume()

# b1.open()

# print(b1.status)
# print(b2.status)

# a="hello"
# b=[1,2,3,4]

# print(type(b1))

# Encapsulation

# class Data:
#     def __init__(self):
#         self.name="Leo"
#         self.__age=53
    
#     def getAge(self):
#         print(self.__age)

# d1=Data()
# print(d1.__age)
# d1.getAge()

# class User:
#     def __init__(self,name,age,userName,password):
#         self.name=name
#         self.age=age
#         self.userName=userName
#         self.__password=password
#     def verifyPass(self,password):
#         return self.__password==password
#     def updatePassword(self,oldPassword,newPassword):
#         if self.__password==oldPassword:
#             self.__password=newPassword
#             print("Changed")
#         else:
#             print("wrong crtedintials..!")
    

# u1=User("Ken",44,"kenken","12345")
# u2=User("Leo",53,"leoleo","54321")
# u3=User("Mia",30,"miamia","67890")


# u1.verifyPass("1245")

# u2.updatePassword("54321","qwerty")
# print(u2.verifyPass("54321"))

# Inheritance

# class Calculator:
#     def __init__(self):
#         self.version="0.0.0"
#     def add(self,a,b):
#         print(a+b)
#     def sub(self,a,b):
#         print(a-b)
#     def mul(self,a,b):
#         print(a*b)
#     def div(self,a,b):
#         print(a/b)

# class UpdatedCalc:
#     def __init__(self):
#         self.version="0.0.1"
#     def mod(self,a,b):
#         print(a%b)
#     def expo(self,a,b):
#         print(a**b)
    
# class SuperCalc(UpdatedCalc,Calculator):
#     def __init__(self):
#         self.version="0.0.2"
#     def cube(self,a):
#         print(a**3)
    
    
# c1=Calculator()

# c2=UpdatedCalc()

# c3=SuperCalc()



# c3.cube(4)


# Abstraction 


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(Vehicle):
#     def start(self):
#         print("Bike is getting started")
#     def stop(self):
#         print("Bike is stopped")
#     def fuel(self):
#         print("Bike is getting fuel")

# class Car(Vehicle):
#     def start(self):
#         print("Car is getting started")
#     def stop(self):
#         print("Car is stopped")
#     def fuel(self):
#         print("Car is getting fuel")

# b1=Bike()
# # b1.start()
# c1=Car()
# c1.fuel()

# print(1+1)
# print("1"+"1")

# method overriding
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat(Dog):
#     def sound(self):
#         print("Meow")
#     # def sound(self):
#     #     print("Bark")

# d1=Dog()
# c1=Cat()

# d1.sound()
# c1.sound()

# method overriding

class Demo:
    def add(self,a,b,c=0):
        print(a+b+c)

d1=Demo()
d1.add(1,2)
d1.add(1,2,3)