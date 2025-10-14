def scoreAlign(a, b, c, align):
    if align == -1:
        if a >= b and a >= c:
            if b >= c:
                print(a, b, c)
            else:
                print(a, c, b)
        elif b >= c:
            if a >= c:
                print(b, a, c)
            else:
                print(b, c, a)
        else:
            if a >= b:
                print(c, a, b)
            else:
                print(c, b, a)
    elif align == 1:
        if a >= b and a >= c:
            if b >= c:
                print(c, b, a)
            else:
                print(b, c, a)
        elif b >= c:
            if a >= c:
                print(c, a, b)
            else:
                print(a, c, b)
        else:
            if a >= b:
                print(b, a, c)
            else:
                print(a, b, c)
   

a = int(input("학생 1 성적 입력: "))
b = int(input("학생 2 성적 입력: "))
c = int(input("학생 3 성적 입력: "))
align = int(input("오름차순 : 1, 내림차순 : -1 : "))

scoreAlign(a,b,c,align)
