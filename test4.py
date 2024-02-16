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

