import json

# Sample Python dictionary

'''
| Function       | Input          | Output                 | Use Case                   |
| -------------- | -------------- | ---------------------- | -------------------------- |
| `json.dumps()` | Python object  | JSON string            | Print/store/send JSON      |
| `json.dump()`  | Python object  | File (with JSON)       | Save data to file          |
| `json.loads()` | JSON string    | Python object          | Parse from string/API      |
| `json.load()`  | File with JSON | Python object          | Read data from file        |
| `default=`     | Custom encoder | JSON-serializable dict | Serialize custom objects   |
| `object_hook=` | Custom decoder | Python object          | Deserialize custom objects |
'''




person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_employee": True,
    "hobbies": ["reading", "cycling"],
    "address": {
        "street": "5th Avenue",
        "zipcode": "10001"
    }
}

print("=== json.dumps() - Convert Python object to JSON string ===")
json_string = json.dumps(person)
print(json_string)

print("\n=== json.dumps() with indent for pretty print ===")
pretty_json = json.dumps(person, indent=4)
print(pretty_json)

print("\n=== json.dump() - Write JSON to file ===")
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

print("JSON written to 'person.json'")

print("\n=== json.loads() - Convert JSON string back to Python object ===")
parsed_person = json.loads(json_string)
print(parsed_person)

print("\n=== json.load() - Read JSON from file and convert to Python object ===")
with open("person.json", "r") as f:
    data_from_file = json.load(f)
    print(data_from_file)

# === Advanced: Encoding custom object ===
print("\n=== Handling custom object using default= in json.dumps() ===")

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

def encode_employee(obj):
    if isinstance(obj, Employee):
        return {"__employee__": True, "name": obj.name, "id": obj.id}
    raise TypeError("Object of type Employee is not JSON serializable")

emp = Employee("Bob", 101)
emp_json = json.dumps(emp, default=encode_employee)
print(emp_json)

print("\n=== Decoding custom object using object_hook= in json.loads() ===")

def decode_employee(dct):
    if "__employee__" in dct:
        return Employee(dct["name"], dct["id"])
    return dct

decoded_emp = json.loads(emp_json, object_hook=decode_employee)
print(f"Decoded Employee: name={decoded_emp.name}, id={decoded_emp.id}")
