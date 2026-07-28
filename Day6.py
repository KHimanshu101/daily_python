# from abc import ABC , abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class rectangle(shape):
#     def area():
#         print("area of the rectangle is 2*length*breadth")

# s1=rectangle
# s1.area()

#question 15
# from abc import ABC , abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def area():
#         print("area of the rectangle is 4a")
# s1=square
# s1.area()

#question 16
# from abc import ABC , abstractmethod 
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class dog(Animal):
#     def sound():
#         print("dog barks")

# s1=dog
# s1.sound()

#question 17
# from abc import ABC, abstractmethod             in this we are importing ABC class from abc module
# class bank:
#     @abstractmethod
#     def interest():
#         pass
# class sbi(bank):
#     def interest():
#         print("this is sbi bank")
# class hdfc(bank):
#     def interest():
#         print("this is hdfc bank")
# s1=sbi
# s2=hdfc
# s1.interest()
# s2.interest()

#question 18
# from abc import ABC, abstractmethod
# class employee(ABC):
#     @abstractmethod
#     def salary():
#         pass
# class manager(employee):
#     def salary():
#         print("manager salary is 500000")
# s1=manager
# s1.salary()

#question 19
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start():
#         pass
# class car(vehicle):
#     def start():
#         print("car starts with key")
# s1=car
# s1.start()

#question 1
# class person:
#     def __init__(self,name,age):
#         self.x=name
#         self.y=age
#     def display(self):
#         print("name:",self.x)
#         print("age:",self.y)
# p1=person('himanshu',20)
# p1.display()

#question 2
# class vehicle:
#     def __init__(self, brand, price):
#         self.x=brand
#         self.y=price
# class car(vehicle):
#     def display(self):
#         print("brand name os car:", self.x)
#         print("price:",self.y)
# class bike(vehicle):
#     def display(self):
#         print("brand name of bike:", self.x)
#         print("price:",self.y)
# s1=car("BMW",10000000)
# s2=bike("royal enfield",250000)
# s1.display()
# s2.display()

#question 3
# class employee:
#     def __init__(self,name,salary):
#         self.x=name
#         self.y=salary
# class manager(employee):
#     def display(self,bonus ):
#         print("manager's name:",self.x)
#         print("salary:",self.y)
#         c= bonus
#         a=self.y+ c
#         print("total salary including bonus:",a)
# s1=manager("himanshu",100000)
# s1.display(50000)


        







