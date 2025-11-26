import json

with open('scripts/Lab005/employees.json', 'r') as f:
    employees = json.load(f)

print(employees)