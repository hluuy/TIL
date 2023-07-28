# # ws_8_1.py

# # 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0
#     def __init__(self):
#         pass
        
# class Dog():
#     pass

# class Cat():
#     pass

# class Pet(Dog, Cat):
   
#    @classmethod
#    def access_num_of_animal(cls):
#        Animal.num_of_animal += 1
#        result = (f'동물의 수는 {Animal.num_of_animal}마리 입니다.')
#        return result

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# # ws_8_2.py

# # 아래 클래스를 수정하시오.
# class Animal:
#    pass

# class Dog(Animal):
#    def bark(self):
#       result = '멍멍 !'
#       return print(result)

   

# dog1 = Dog()
# dog1.bark()

# # ws_8_3.py

# # 아래 클래스를 수정하시오.
# class Animal:
#    pass

# class Cat(Animal):
#    def meow(self):
#       result = '야옹 !'
#       return print(result)

# cat1 = Cat()
# cat1.meow()

# # ws_8_4.py

# class Animal:
#    pass

# class Dog(Animal):
#    def bark(self):
#       result = '멍멍 !'
#       return print(result)


# class Cat(Animal):
#    def meow(self):
#       result = '야옹 !'
#       return print(result)
   
   
# class Pet(Dog, Cat):
#    def __init__(self, text):
#       self.text = text
   
#    def make_sound(self):
#       sound = print(self.text)
#       return sound
   
#    def play(self):
#       result = print('애완동물과 놀기')
#       return result
   

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()

# # ws_8_5.py
# class Dog:
#     sound = '멍멍'


# class Cat:
#     sound = '야옹'


# class Pet(Dog, Cat):
#     def __str__(self):
#         return f'애완동물은 {self.sound}소리를 냅니다.'

# pet1 = Pet()
# print(pet1)

# # hw_8_2.py

# # 아래 함수를 수정하시오.
# def check_number():
#     try:
#         num = int(input('숫자를 입력하세요: '))
#         if num >= 1:
#             print('양수입니다.')
#         elif num == 0:
#             print('0입니다.')
#         elif num <= -1:
#             print('음수입니다.')
#     except ValueError:
#         print('잘못된 입력입니다.')


# check_number()

# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    
    def get_user_info(self):
        get_name = input('이름을 입력하세요: ')
        self.user_data['name'] = get_name
        try:
            get_age = int(input('나이를 입력하세요: '))
            self.user_data['age'] = get_age
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
            return
        



    def display_user_info(self):
        try:
            print('사용자 정보 :')
            print(f'이름: {self.user_data["name"]}')
            print(f'나이: {self.user_data["age"]}')
        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()

