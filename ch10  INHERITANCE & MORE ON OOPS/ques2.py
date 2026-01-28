class animal:
    def speak(self):
        return "Animal speaks"
class pet(animal):
    def speak(self):
        return "Pet barks"
class dog(pet):
    def speak(self):
        return "Dog barks loudly"
o=animal()
print(o.speak())    
p=pet()
print(p.speak())
q=dog()
print(q.speak())
