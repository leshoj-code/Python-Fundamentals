class Student:
    def __init__(self, fullName, course, age, feesPaid):
        self.fullName = fullName
        self.course = course
        self.age = age
        self.feesPaid = feesPaid

    def work(self):
        print(self.fullName,"Loves to study")

stud1 = Student("Omondi Timon","Data Science",21,25000.00)
print("Name:",stud1.fullName,"Course enrolled:", stud1.course,"Age:", stud1.age,"Fees Paid:", stud1.feesPaid)
print()

stud2 = Student("Douglas Waweru","MIT",19,37250.00)
print("Name:",stud2.fullName,"Course enrolled:", stud2.course,"Age:", stud2.age,"Fees Paid:", stud2.feesPaid)
print()

stud3 = Student("Nigel Cheloti","CyberSecurity",18,40000.00)
print("Name:",stud3.fullName,"Course enrolled:", stud3.course,"Age:", stud3.age,"Fees Paid:", stud3.feesPaid)
print()

stud4 = Student("Wanjigi Jimmy","MIT",21,29333.00)
print("Name:",stud4.fullName,"Course enrolled:", stud4.course,"Age:", stud4.age,"Fees Paid:", stud4.feesPaid)
print()

stud5 = Student("David Lingard","CyberSecurity",20,20100.00)
print("Name:",stud5.fullName,"Course enrolled:", stud5.course,"Age:", stud5.age,"Fees Paid:", stud5.feesPaid)
print()