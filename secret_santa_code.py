import csv
import random
from typing import List, Dict, Tuple

class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.secret_child = None

class SecretSantaAssigner:
    def __init__(self, employees: List[Employee], prev_assignments: Dict[str, str]):
        self.employees = employees
        self.prev_assignments = prev_assignments

    def assign_secret_santa(self):
        available_children = [e for e in self.employees]
        random.shuffle(available_children)
        
        for giver in self.employees:
            valid_children = [child for child in available_children if child.name != giver.name and child.name != self.prev_assignments.get(giver.name)]
            
            if not valid_children:
                raise ValueError("Cannot assign secret santa without violating constraints. Try again.")
            
            secret_child = random.choice(valid_children)
            giver.secret_child = secret_child
            available_children.remove(secret_child)

    def get_assignments(self) -> List[Tuple[str, str, str, str]]:
        return [(e.name, e.email, e.secret_child.name, e.secret_child.email) for e in self.employees]

class FileHandler:
    @staticmethod
    def read_employee_file(file_path: str) -> List[Employee]:
        employees = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        return employees

    @staticmethod
    def read_previous_assignments(file_path: str) -> Dict[str, str]:
        prev_assignments = {}
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    prev_assignments[row['Employee_Name']] = row['Secret_Child_Name']
        except FileNotFoundError:
            pass
        return prev_assignments

    @staticmethod
    def write_output_file(file_path: str, assignments: List[Tuple[str, str, str, str]]):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
            writer.writerows(assignments)

def main():
    input_file = 'employees.csv'
    prev_assignments_file = 'previous_assignments.csv'
    output_file = 'secret_santa_assignments.csv'
    
    employees = FileHandler.read_employee_file(input_file)
    prev_assignments = FileHandler.read_previous_assignments(prev_assignments_file)
    
    assigner = SecretSantaAssigner(employees, prev_assignments)
    assigner.assign_secret_santa()
    
    assignments = assigner.get_assignments()
    FileHandler.write_output_file(output_file, assignments)
    
    print("Secret Santa created!")

if __name__ == "__main__":
    main()
