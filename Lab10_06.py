scores = ( ('Jhon', 88, 95, 90), ('Mina', 85, 90, 95),
('Lia', 70, 90, 80), ('Peter', 90, 90, 95))

score_dic = {}
for stu in scores:
    score_dic[stu[0]] = (stu[1] + stu[2] + stu[3]) / 3.0

print("Name\t\tAverage Grade")
print("-----------------------------")
for k,v in score_dic.items():
    print("%s\t\t%.2f" %(k,v))
