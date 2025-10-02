pw = input("Enter your secret code: ")
cnt = 0

if pw.startswith("SEC"):
    cnt+=1

if pw.endswith("123"):
    cnt+=1

if pw.count("@"):
    cnt+=1

if cnt == 3:
    print("Access Granted!")
elif cnt == 2:
    print("Almost there, try again")
else:
    print("Access Denied")
