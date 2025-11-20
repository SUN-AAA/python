event_attendance = {"Seminar": ["S01", "S02", "S03", "S04"], 
                    "AI Workshop": ["S02","S03"], 
                    "Job Fair": ["S01", "S03", "S05"], 
                    "Hackathon": ["S03", "S04", "S06", "S02"]}

print("== Converted to a dictionary with sets ==")
print(event_attendance)
print("")

seminar = set(event_attendance["Seminar"])
aiWorkshop = set(event_attendance["AI Workshop"])
jobFair = set(event_attendance["Job Fair"])
hackathon = set(event_attendance["Hackathon"])

all = seminar & aiWorkshop & jobFair & hackathon
print("Student who attended All events:",all)
print("")

uni = seminar | aiWorkshop | jobFair | hackathon
print("Students who attended ANY events:",uni)
print("")

attendence_count = {}
for v in event_attendance.values():
    for stu in v:
        if stu in attendence_count:
            attendence_count[stu] += 1
        else:
            attendence_count[stu] = 1
    
print("Attendance count:",attendence_count)
print("")

top1_v = 0
top2_v = 0

for k,v in attendence_count.items():
    if v >= top1_v:
        top1_v = v
        top1_k = k 
    elif v >= top2_v:
        top2_v = v
        top2_k = k

top1 = (top1_k,top1_v)
top2 = (top2_k,top2_v)

print(f"Top 2 most active students: [{top1}, {top2}]")

