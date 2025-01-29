class Human:

    def __init__(self, name: str, age: int): # метод дает инициализацию, даем характеристики объекту
        self.name = name
        self.age = age

    def walk(self, km):
        if km > 5:
            return f'{self.name} не может пройти {km} км'
        else:
            return f'{self.name} может пройти {km} км'

human = Human(name='Петя', age=25)
km = int(input('Введите кол-во км: '))
print(human.walk(km=km))
print(human.name)
print(human.age)

human2 = Human(name='Вася', age=25)
km = int(input('Введите кол-во км: '))
print(human2.walk(km=km))
print(human2.name)
print(human2.age)

# human = Human()
# km = int(input('Введите кол-во км: '))
# print(human.walk(km=km))

"""
Human.walk(human, km)
"""
