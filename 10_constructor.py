class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary =salary
        self.subunit=subunit
        print("Employee is created")

    def getdetails(self):
        print(f'The name is Employee is {self.name}')
        print(f'The salary is Employee is {self.salary}')
        print(f'The subunit is Employee is {self.subunit}')


    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morning,love")

    @staticmethod
    def time():
        print("The time is 9PM in the evening")


dejal=Employee("Dejal", 1200 , "Youtube")
# dejal  =  Employee()  -->This throws an error
dejal.getdetails()