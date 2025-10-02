file = input("Enter the file name: ")

if file.endswith(".png"):
    idx = file.rfind(".png")
    print(f"{file[:idx]}.jpg")
else:
    print(file)