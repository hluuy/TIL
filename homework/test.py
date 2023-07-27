# 캡슐화
# class Student():
#     def __init__(self, name, age, id, grade):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.grade = grade

# Lee = Student('Lee', 24, '2046318131', 4.3)
# print(Lee.name)
# print(Lee.age)
# print(Lee.id)
# print(Lee.grade)

# # -----
# class Student():
#     def __init__(self, name, age, id, grade):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.grade = grade

# Lee = Student('Lee', 24, '2046318131', 4.3)
# print(Lee.name)
# print(Lee.age)
# print(Lee.id)
# print(Lee.grade)
# Lee.grade = 4.5
# print(Lee.grade)

# #-----------
# #23분
# class Student():
#     def __init__(self, name, age, id, grade):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.__grade = grade

# Lee = Student('Lee', 24, '2046318131', 4.3)
# print(Lee.name)
# print(Lee.age)
# print(Lee.id)
# print(Lee.grade)
# #__ 두개로 캡슐화하여 수정도 조회도 못함
# #메서드를 만들어야함
# #-----------

# class Student():
#     def __init__(self, name, age, id, grade):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.__grade = grade

#     def get_grade(self):
#         return self.__grade

# Lee = Student('Lee', 24, '2046318131', 4.3)
# print(Lee.name)
# print(Lee.age)
# print(Lee.id)
# # print(Lee.grade)
# grade = Lee.get_grade()
# print(grade)

# #게터 함수
# 세터 함수는 알아서 알아봐

#다형성

# class Animal():
#     def __init__(self, name):
#         self.name = name
    
#     def bark(self):
#         print('울음소리')

# class Cat(Animal):
#     def bark(self):
#         return '냐옹'
    
# class Dog(Animal):
#     def bark(self):
#         return '멍멍'
    
# class Pig(Animal):
#     def bark(self):
#         return '꿀꿀'
    
# cat = Cat('나비')
# dog = Dog('누렁이')
# pig = Pig('꿀꿀이')

# print(cat.bark())
# print(dog.bark())
# print(pig.bark())

# #---------------------
# 38분 언저리
# class Person():
#     def __init__(self, name, height, weight, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age

#     def walk(self):
#         return f'{self.name}은 걷는다'

# hw_7_2.py

# class StringRepeater:
#    def repeat_string(self, count, string):

#       for _ in range(count):
#         print(string)


# repeater1 = StringRepeater()
# repeater1.repeat_string(3, 'Hello')
# class Person:
#    number_of_people = 0
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       self.__class__.number_of_people += 1

#    def introduce(self):
#         print(f'제 이름은 {self.name}이고, 저는 {self.age} 살 입니다.')

#    @classmethod
#    def get_number_of_people(cls):
#       return cls.number_of_people
  
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)
# person2 = Person("duke", 30)
# person2.introduce()
# print(Person.get_number_of_people())

class Shape():
   def __init__(self, width, height):
      self.a = (width, height)
   
   def calculate_area(self):
      return self.a[0] * self.a[1]


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)