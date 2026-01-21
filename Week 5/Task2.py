import json
with open("myjava.json", "r") as f:
    data = json.load(f)
for student in data:
    marks = student["grades"]
    avg = sum(marks) / len(marks)
    student["average_grade"] = avg
with open("updated.json", "w") as out:
    json.dump(data, out, indent=4)
