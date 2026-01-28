class Employee:
    salary=10000
    increment=150
    @property
    def salary_after_increment(self):
        return self.salary + self.salary * (self.increment/100)
    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment=((salary/self.salary)-1)*100
emp=Employee()
print(emp.salary_after_increment)
emp.salary_after_increment=12000
print(emp.increment)