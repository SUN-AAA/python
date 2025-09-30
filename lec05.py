my_string = "hello world with ,my dear friends"

#type()
print(type(my_string))

#len()
print(len(my_string))

#index positive
print(my_string[10])

#index negative
print(my_string[-1])

#index len
print(my_string[len(my_string) - 1])

#수정 불가 - error
"""my_string[0] = 'H'
print(my_string)"""

#명령어 - startswith()
print(my_string.startswith('a'))
print(my_string.startswith('h'))

#명령어 - endswith()
print(my_string.endswith('s'))
print(my_string.endswith('a'))

#in 활용
print("wor" in my_string)

#index
print(my_string.index("world"))
print(my_string.index('h', 0, 7))

#find
print(my_string.find("world"))
print(my_string.find("world", 5, 10))

#추출 - [:]
sub_word = my_string[2:5]
print(sub_word)

sub_word = my_string[:5]
print(sub_word)

sub_word = my_string[:]
print(sub_word)

#제거 - strip()
print(my_string.strip())
print(my_string.strip('h'))
print(my_string.strip("hello"))

print(my_string.lstrip('h'))
print(my_string.rstrip('s'))

#치환
new_string = "Hot coffee"
print(new_string)
print(new_string.replace("Hot", "Cold"))

#기타 명령어
#isalnum() : 문자열이 알파벳과 숫자로만 구성되어 있는지 확인
engstr = "Hi friends"
numstr = "222"

print(numstr.isalnum())
print(engstr.isalnum())

#isalpha() : 문자열이 알파벳만으로 구성되어 있는지 확인
print(engstr.isalpha())
print(numstr.isalnum())

#isdigit(), isnumeric() : 문자열의 글자가 숫자로만 구성되어 있는지 확인
#islower() : 문자열이 영문 소문자로만 구성되어 있는지 확인
#isupper() : 문자열이 영문 대문자로만 구성되어 있는지 확인
#upper() : 문자열을 대문자로 변환된 새로운 문자열 반환
#lower() : 문자열을 소문자로 변환된 새로운 문자열 반환
#swapcase() : 문자열의 대문자는 소문자로 변환, 소문자는 대문자로 변환된 새로운 문자열 반환
#count(str) : 문자열에서 주어진 문자열인 str이 몇 번 나오는지 반환
#count(str, start, end) : 문자열에서 주어진 문자열인 str이 몇 번 나오는지 찾는데 start 부터 end – 1 인덱스내에서만 검색

