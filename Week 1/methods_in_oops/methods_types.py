class Employee:
    total_employees = 0
    def __init__(self, name: str, dept: str, salary: int) -> None:
        if not Employee.is_valid_salary(salary):
            raise ValueError(f"Salary ${salary} violates company policy ($20k - $50k).")
        self.name = name
        self.dept = dept
        self.salary = salary
        Employee.total_employees += 1

    def __str__(self) -> str:
        return f"{self.name} | {self.dept} | {self.salary} "
    
    @classmethod
    def get_total_employees(cls) -> int:
        return cls.total_employees

    @staticmethod
    def is_valid_salary(salary: int) -> bool:
        min_sal, max_sal = 20000, 500000
        return min_sal <= salary <= max_sal

    @classmethod
    def from_string(cls, data: str) -> str:
        name, dept, sal = data.split("-")
        return cls(name, dept, int(sal))

    
        
e1 = Employee("Arjun", "Finance", 45000)
e2 = Employee.from_string("Riya-Engineering-85000")

print(Employee.get_total_employees())  # 2
print(Employee.is_valid_salary(15000)) # False
print(Employee.is_valid_salary(45000)) # True
print(e1)                              # Arjun | Finance | ₹45000
print(e2)
