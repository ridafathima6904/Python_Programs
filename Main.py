# # # # # # # # # import math 
# # # # # # # # # import Calculator
# # # # # # # # # print(math.sqrt(25))
# # # # # # # # # print(math.factorial(5))
# # # # # # # # # print(math.pi)

# # # # # # # # # result=calculator,add
# # # # # # # # # print(result)


# # # # # # # # # try:
# # # # # # # # #     a=int(input())
# # # # # # # # #     b=int(input())
# # # # # # # # #     print(a//b)
# # # # # # # # # except ValueError:
# # # # # # # # #     print("Please enter integer only")
# # # # # # # # # except ZeroDivisionError:
# # # # # # # # #     print("cannot divide by zero")
# # # # # # # # # finally:
# # # # # # # # #     print("something")            


# # # # # # class Student:
# # # # # #     name="Rahul"
# # # # # #     age=20
# # # # # #     def marks(self):
# # # # # #         print("Tamil: 89,English: 90")
# # # # # # s1=Student()
# # # # # # print(s1.name)
# # # # # # print(s1.age)
# # # # # # s1.marks()        


# # # # # # # class student:
# # # # # # #     name="Unknown"
# # # # # # #     mark=0

# # # # # # #     def display(self):
# # # # # # #         print("Name: ",self.name)
# # # # # # #         print("Mark: ",self.mark)
# # # # # # # s1=student()
# # # # # # # s1.name="naveen"
# # # # # # # s1.mark=90
# # # # # # # s2=student()      
# # # # # # # s2.name="praveen"
# # # # # # # s2.mark=98
# # # # # # # s3=student()
# # # # # # # s3.name="praveena"
# # # # # # # s3.mark=89
# # # # # # # s1.display()
# # # # # # # s2.display()
# # # # # # # s3.display()  


# # # # # # class student:
# # # # # #     name="unknown"
# # # # # #     mark=0
# # # # # #     def __init__(self,name,mark):
# # # # # #         self.name=name
# # # # # #         self.mark=mark

# # # # # #     def display(self) :
# # # # # #         print("name: ",self.name)
# # # # # #         print("mark: ",self.mark)

# # # # # # s1=student("naveen",89)
# # # # # # s1.display()        


# # # # # class Device:
# # # # #     def power_on(self):
# # # # #         print("Device switched on")
# # # # # class Phone(Device):
# # # # #     def call(self)
# # # # #     print("making a phone call")
# # # # # samsung=Phone()
# # # # # samsung.call()
# # # # # samsung.power_on()
# # # # # print()

# # # # # class Device:
# # # # #     def power_on(self):
# # # # #         print("Device switched on")
# # # # # class computer(Device):
# # # # #     def run_program(self):
# # # # #         print("running a python program")
# # # # # class laptop(computer):
# # # # #     def charge(self):
# # # # #         print("laptop battery charging")
# # # # #         asus=laptop
# # # # #         asus.power_on()
# # # # #         asus.run_program()
# # # # #         asus.charge()
# # # # #         print()

# # # # # class camera:
# # # # #     def take_photo(self):
# # # # #         print("Taking a photo")
# # # # # class musicplayer:
# # # # #     def playmusic(self):
# # # # #         print("Playing music")
# # # # # class smartphone(camera,musiccplayer):
# # # # #     def call(self):
# # # # #         print("Making a phone call")
# # # # # mi=smartphone()
# # # # # mi.playmusic()
# # # # # mi.take_photo()
# # # # # mi.call()
# # # # # print()
# # # # # #hierarchical inheritance one parent multiple child
# # # # # # class Device:
# # # # # #     def power_on(self):
                                
            


# # # # #polymorphism many forms
# # # # # #method overriding
# # # # # class Phone:
# # # # #     def camera(self):
# # # # #         print("taking a normal photo")
# # # # # class smartphone(Phone):
# # # # #     def camera(self):
# # # # #         print("taking a potrait photo")
# # # # # mi=smartphone()
# # # # # mi.camera()
# # # # # nokia=Phone()
# # # # # nokia.camera()
# # # # # print()

# # # # #encapsulation

# # # # # class Phone:
# # # # #     __battery="30%"
# # # # #     def printbattery(self):
# # # # #         print(self.__battery)
# # # # # iphone15=Phone()
# # # # # iphone15.printbattery()        
        

# # # # #abstractn

# # # # from abc import ABC,abstractmethod
# # # # class payment(ABC):
# # # #     @abstractmethod
# # # #     def pay(self):
# # # #         pass
# # # # class UPI(Payment):
# # # #     def pay(self):
# # # #     print("Payment completed using UPI")
# # # # class GPay(Payment):
# # # #     def pay(self):
# # # #     print("payment completed using gpay")
# # # # class Phonepe(Payment):
# # # #     def pay(self):
# # # #     print("payment completed using phonepe")
# # # # Payment=UPI()    
# # # # Payment.pay()
# # # # Payment=GPay()
# # # # Payment.pay()
# # # # Payment=Phonepe()
# # # # Payment.pay()            


# # # #time and space complexity
# # # #time  complexity describes how number of operations an algorithm performs as its input size increases
# # # #it measures the growth rather than exact running time in second
# # # #o(1)-constant time
# # # names=["rahul","naveen","peter","praveen"]
# # # print(names[2])
# # # print(names[3])
# # # #linear time - o(n)
# # # n=100
# # # for i in range(n):
# # #     print(i,end=" ")
# # # #quadratic - o(n)
# # # num=5
# # # for i in range(1,num+1):
# # #     for j in range(1,num+1):
# # #         print(j,end=" ")
# # #     print()
# # # #logarithmic o(log n)
# # # nums=16        
# # # while nums>1:
# # #     print(nums)
# # #     nums//=2
# # # #space complexity describes how the memory recuired by an algorithm grows as its input size increases
# # # #extra space means additional memory used excluding existing input
# # # #o(1) constant space 
# # # listone=[4,6,7,82,1,9,0,3,5,6]
# # # total=0
# # # for value in listone:
# # #     total+=value
# # # print(total)
# # # #linear space o(n)
# # # listtwo=[1,2,3,4]
# # # temp=[]
# # # for values in listtwo:
# # #     temp.append(values*values)       
# # # print(temp)    


# # n=int(input())
# # listone=[]
# # for i in range(n):
# #     data=int(input())
# #     listone.append(data)
# # left=0
# # right=len(listone)-1
# # while left<right:
# #     temp=listone[left]
# #     listone[left]=listone[right]
# #     listone[right]=temp
# #     left+=1
# #     right-=1
# # print(listone)        


# #with using thid variable

# # a=10
# # b=20
# # print(a," ",d)
# # c=c+d
# # d=c-d
# # c=c-d
# # print(c,"",d)

# #move zeros

# def movezeros(arr):
#     j=0
#     for i in range(len(arr)):
#         if arr[i]!=0:
#             arr[j]=arr[i]
#             j+=1
#     while j<len(arr):
#         arr[j]=0
#         j+=1 
#     print(arr)

# arr=[3,0,5,4,0,0,9]
# movezeros(arr)                


#linear search 
listtwo=[5,1,4,2,8]
find=200
found=False
for i  in range(len(listtwo)):
    if listtwo[i]==find:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")    
            