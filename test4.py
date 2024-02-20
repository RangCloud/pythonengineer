class ClassicCar:
    def drive(self):
        print("수동 운전 모드!")

father = ClassicCar()
father.drive()
print()

class NewCar:
    color = "빨간색"
    
    def test(self):
        color = "파란색"
        print("color = ", color)
        print("self.color = ", self.color)

son = NewCar()
son.test()
son.color = "검은색"
son.test()
print()

class SecondCar:
    def __init__(self, color):
        self.color = color
        
    def test(self):
        print(self.color)
        
moon = SecondCar("빨간색")
print(moon.color)
moon.color = "검은색"
print(moon.color)
print()

class Car:
    __cnt = 0
    
    def __init__(self, color):
        self.color = color;
        Car.__cnt += 1
        print(Car.__cnt, "번째 인스턴스 생성");
        
c1 = Car("핑크");
c2 = Car("파랑");
print(c1.color,"자동차");

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def welcome(self):
        print("환영합니다.", self.name, "님!");
        
x = Student("이기적", 36);
x.welcome()