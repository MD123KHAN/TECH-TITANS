import random

sample_cases = []

case_types = ["Criminal", "Civil", "Family", "Corporate", "Property"]
lawyer_status = ["Available", "Absent"]

start_id = 1000

for i in range(500):
    case = {
        "id": f"C{start_id + i}",
        "type": random.choice(case_types),
        "age": round(random.uniform(0.5, 5.0), 2),
        "adj": random.randint(0, 10),
        "lawyer": random.choice(lawyer_status)
    }
    sample_cases.append(case)

# Print dataset in same list-of-dictionary format
print("sample_cases = [")
for case in sample_cases:
    print(f'{case},')
print("]")
