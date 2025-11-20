students = {"Jhon": {"Math", "Physics"}, 
            "Mina": {"English", "Math"}, 
            "Lia": {"Biology"}, 
            "Alex": {"Math", "Biology", "English"}}

course = input("Enter a course name: ")
student = set()
cnt = 0

for k,v in students.items():
    if course in v:
        student.add(k)
        cnt = 1

if cnt != 1:
    print("No student found.")
else:
    print(f"Student taking {course}: {student}")