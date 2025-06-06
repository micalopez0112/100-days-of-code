
class Animal():
    def __init__(self, name):
        self.name = name
        
    def breath(self):
        print(f'{self.name} is breathing')

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def breath(self):
        super().breath()
        print(f'{self.name} is breathing under the water')
        
    def swim(self):
        print(f'{self.name} is swimming')
        
nemo = Fish('Nemo')
nemo.breath()
nemo.swim()
print(nemo.name)