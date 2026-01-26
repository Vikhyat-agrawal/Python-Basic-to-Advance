class Programmer:
    def __init__(self,name,language,exp):
        self.name = name
        self.language = language
        self.exp = exp

p=Programmer("Ayush","Python","2 years")
print(p.name,p.language,p.exp)
r=Programmer("Rohan","Java","5 years")
print(r.name,r.language,r.exp)