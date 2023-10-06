"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

       
class Commission:
    def __init__(self, commision, contracts):
        self.commision =commision
        self.contracts = contracts
    def calculate_commision(self):
        if self.contracts > 0:
            return self.commision * self.contracts
        return self.commision
    
class SalaryContract(Commission):
    def __init__(self, salary, commision = 0, contracts = 0):
        super().__init__(commision,contracts)
        self.salary = salary
    def calculate_pay(self):
        if self.commision > 0:
            return self.salary + super().calculate_commision()
        else:
            return self.salary
    def __str__(self):
        if self.contracts > 0:
            return f"monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commision}/contract."
        if self.commision > 0:
            return f"monthly salary of {self.salary} and receives a bonus comission of {self.commision}."
        return f"monthly salary of {self.salary}."
        
class HourlyContract(Commission):
    def __init__(self, hours, rate, commision = 0, contracts = 0):
        super().__init__(commision,contracts)
        self.hours = hours
        self.rate = rate
    def calculate_pay(self):
        if self.commision > 0:
            return (self.hours * self.rate) + super().calculate_commision()
        else:
            return self.hours * self.rate
    def __str__(self):
        if self.contracts > 0:
            return f"contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commision}/contract."
        if self.commision > 0:
            return  f"contract of {self.hours} hours at {self.rate}/hour and receives a bonus comission of {self.commision}."
        return f"contract of {self.hours} hours at {self.rate}/hour."


class Employee:
    def __init__(self, name, contract: object):
        self.name = name
        self.contract =contract

    def get_pay(self):
        return self.contract.calculate_pay()

    def __str__(self):
        return self.name +" works on a " + self.contract.__str__() + f" Their total pay is {self.get_pay()}."



    



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_pay = SalaryContract(4000)
billie = Employee('Billie', billie_pay)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_pay = HourlyContract(100, 25)
charlie = Employee('Charlie', charlie_pay)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_pay = SalaryContract(3000, 200, 4)
renee = Employee('Renee', renee_pay)
print(renee)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_pay = HourlyContract(150, 25, 220, 3)
jan = Employee('Jan', jan_pay)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_pay = SalaryContract(2000, 1500)
robbie = Employee('Robbie', robbie_pay)
print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_pay = HourlyContract(120, 30, 600)
ariel = Employee('Ariel', ariel_pay)

