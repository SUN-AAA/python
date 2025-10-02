nums = input("Enter 3 inegers seperated by commas: ")
comma1 = nums.find(',')
comma2 = nums.rfind(',')

num1 = int(nums[:comma1])
num2 = int(nums[comma1+1:comma2])
num3 = int(nums[comma2+1:])

print("Ordered numbers: ", end="")
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
else:
    if num1 >= num2:
        print(num2, num1, num3)
    else:
        print(num1, num2, num3)
    


