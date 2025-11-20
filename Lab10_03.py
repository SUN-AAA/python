guPopulation = "강남구,233363,강동구,199088,강북구,144410,강서구,267442,관악구,273736,광진구,166638,구로구,180027,금천구,114402,노원구,217272,도봉구,138120"
pop = guPopulation.split(",")
popDic = {}

for key in range(0,20,2):
    popDic[pop[key]] = pop[key+1]


n = int(input("Enter the population to compare: "))
cnt = 0

for key,val in popDic.items():
    if int(val) < n:
        print(f"District with a population less than {n}")
        print(f"{key}:{val}")
        cnt = 1

if cnt != 1:
    print(f"There is no district with a population less than {n}")