def secondWord(s):
    s = s.strip()
    
    idx1 = s.find(" ")
    new_s = s[idx1 + 1:]

    new_s = new_s.strip()
    idx2 = new_s.find(" ")
    
    if idx2 == -1:
        res_s = new_s
    else:
        res_s = new_s[:idx2 + 1]
    
    return res_s

s = input("두 개 이상의 단어가 있는 문자열 입력 : ")
print(secondWord(s))
