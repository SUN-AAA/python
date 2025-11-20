student_tuple = (('191101', 'Jhon', '010-123-45xx'), ('191102','Mina', '010-223-45xx'), ('191103', 'Lia', '010-323-45xx'))
student_dic = {}

for student in student_tuple:
    student_dic[student[0]] = student[1]

print(f"Student Information : {student_dic}")

while True:
    num = input("Enter tyour student number: ")
    if int(num) < 0:
        print("Quit the program.")
        break

    if num in student_dic.keys():
        print(f"Student number {num} is {student_dic[num]}")
    else:
        print("There is no student with that number.")