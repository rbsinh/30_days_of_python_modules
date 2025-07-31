import yaml

# Sample Python object
person = {
    "name": "Alice",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "Machine Learning"],
    "address": {
        "street": "5th Avenue",
        "city": "New York"
    }
}

print("=== Dump Python object to YAML string ===")
yaml_string = yaml.safe_dump(person)
print(yaml_string)

print("\n=== Write YAML to file ===")
with open("person.yaml", "w") as f:
    yaml.safe_dump(person, f)

print("Written to person.yaml")

print("\n=== Load YAML from string ===")
yaml_input = """
name: Bob
age: 25
hobbies:
  - guitar
  - chess
"""
data = yaml.safe_load(yaml_input)
print(data)

print("\n=== Load YAML from file ===")
with open("person.yaml", "r") as f:
    data_from_file = yaml.safe_load(f)
    print(data_from_file)

print("\n=== Load multiple YAML documents from string ===")
multi_doc_yaml = """
---
name: Alice
role: Developer
---
name: Bob
role: Manager
"""
docs = yaml.safe_load_all(multi_doc_yaml)
for doc in docs:
    print(doc)

# === Advanced: Custom object ===
print("\n=== Custom Python object to YAML ===")

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def __repr__(self):
        return f"Employee(name={self.name}, emp_id={self.emp_id})"

def employee_representer(dumper, obj):
    return dumper.represent_mapping('!Employee', {'name': obj.name, 'emp_id': obj.emp_id})

yaml.add_representer(Employee, employee_representer)

emp = Employee("Charlie", 101)
emp_yaml = yaml.dump(emp)
print(emp_yaml)

# Optional: load back using custom constructor (not shown for safety)

