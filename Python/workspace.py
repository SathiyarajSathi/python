#1
"""class Person():
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
"""


#2
"""
class parent:
  def __init__(sathi,name,age):
    sathi.name = name
    sathi.age = age
  def teacher(fine):
    print("Im there {}".format(fine.name))
class child(parent):
 # def __init__
  pass

p1=child("sathi",18)
print(p1.name)
p=parent("tech",21)
p.teacher()
"""


#3
"""
class parent:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def teacher(self):
    print("Im there {}".format(self.name))

class child(parent):
  def __init__(self):
    #self.height=height
    super().__init__(name,age)
  

p=parent("raj",20)
p.teacher()
print(p.name)
p1=child()
print(p1.name)
"""


#4
"""
n = int(input())
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and 2<n<5:
    print("Not Weird")
elif n%2 == 0 and 6 < n <= 20:
    print("Weird")
elif n%2 == 0 and n >20:
    print("Not Weird")
"""

#5
"""
def is_leap(year):
    
    n=year/4
    
    if n%2==0:
        leap = True
    else:
        leap = False    
    return leap

    
year = int(input())
print(is_leap(year))
"""

#6
"""
n = int(input())
a=""
for i in range(1,n+1):
    (a)=str(a)+str(i)
print(a)
"""


#7
"""
from itertools import permutations
print(permutations("HACK",r=2))
"""

#8
def flower_dict(filename):
    flow_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flow_dict[letter] = flower
    return flow_dict
def find_word():
    file_name = flower_dict("P:flow.json")
    user_input = str(input("Enter your first name and last name only:"))
    ans= user_input[0].lower()
    print("Flower named from your first letter {}".format(file_name[ans]))

    
find_word()
