# ws_7_1.py

# 아래 클래스를 수정하시오.
class Shape():
   def __init__(self, width, height):
      
      self.width = width
      self.height = height
      
shape1 = Shape(5, 3)
print(shape1.width, shape1.height)

# ws_7_2.py

# 아래 클래스를 수정하시오.
class Shape():
   def __init__(self, width, height):
      self.width = width
      self.height = height
   
   def calculate_area(self):
      area = self.width * self.height
      return area


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)

# # ws_7_3.py

# # 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, width, length):
      self.width = width
      self.length = length

   def calculate_perimeter(self):
      result = (self.width + self.length) * 2
      return result
      

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)

# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, width, height):
      self.width = width
      self.height = height
    
   def print_info(self):
      get_width = self.width
      get_height = self.height
      get_area = self.width * self.height
      get_perimeter = (self.width + self.height) * 2
      result = f'Width: {get_width}\nHeight: {get_height}\nArea: {get_area}\nPerimeter: {get_perimeter}'
      return result
      

shape1 = Shape(5, 3)
shape1.print_info()
print(shape1.print_info())

# ws_7_5.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, width, height):
      self.width = width
      self.height = height

   def __str__(self):
      return f'Shape: width={self.width}, height={self.height}'

shape1 = Shape(5, 3)
print(shape1)

# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   def __init__(self, count, text):
      self.count = count
      self.text = text

   def repeat_string(self):
      i = 0
      while i < self.count:
         print(self.text)
         i += 1

repeater1 = StringRepeater(3, "Hello")
repeater1.repeat_string()

# hw_7_4.py

# 아래 클래스를 수정하시오.
class Person:
   number_of_people = 0
   def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.number_of_people += 1

   def introduce(self):
        print(f'제 이름은 {self.name}이고, 저는 {self.age} 살 입니다.')
  
person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
