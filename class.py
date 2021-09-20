class Student:
    subj=6
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def rcall(self):
        print(f'{self.name} and {self.age}')
    def birthday(self):
        print(f'{self.name} birthday is {2021-self.age}')
    @classmethod
    def Common(cls):
        print(f'all student have {cls.subj} subjects')

# s1=Student("mg mg",13)
# s1.rcall()
# s1.birthday()
Student.Common()