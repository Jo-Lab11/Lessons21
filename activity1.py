student_data = {
    "id1": {"name": "Sara", "class": "v", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "v", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "v", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "v", "subject_integration": "english, math, science"}
}

result = {}
seen = []

for id, data in student_data.items():
    key = (data["name"], data["class"], data["subject_integration"])
    if key not in seen:
        seen.append(key)
        result[id] = data

for k, v in result.items():
    print(k, ":", v)