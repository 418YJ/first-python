#문자열 문자열 인덱스는 첫칸은 0부터 시작, 음수로 할때는 마지막 칸이 -1까지
text='abc'
text[0] == text[-3]
text[1] == text[-2]
text[2]==text[-1]

#문자열 슬라이스
text='abcde fgh ijk'
print(text[2:5]) #문자를 자를때는 자를 인덱스번호의 다음번호까지로!
print(text[:])

#하나 더! 세번쨰 : 뒤에는 간격을 의미함 2를 쓰면 두칸마다 문자를 슬라이스해서 가지고 옴
print(text[0:8:2])

#음수를 쓸때는?
print(text[0:8:-1]) #이렇게 하면 공백만 출력됨 범위가 맞지 않기 때문! 세번째자리 음수는 text 뒤에서부터 타고 내려옴.
print(text[8:0:-1]) #두번째 숫자 뒤에있는 숫자까지만 해당됨
#진행방향 정방향일때는 숫자 +1, 역방향은 -1로 쓰기
print(text[::-1]) #생략하면 역방향

#문자열 매소드
## 출력 지정: formet(a,b,c....) -빈칸 채우기 가능

text='abcde {} {}'
print(text.formet('ABC', 123))

## 대체하기: replace(a,b) a를 b로 대체
text='abcde ABC ABC'
print(text.replace('A','K')) 

##자르기:split(a)-괄호안에 자르고자하는 구분사 넣기.
text = 'abcde A/B/C A.B.C'
a,b,c=text.split()#공백을 두면 공백 기준으로 잘라서 출력됨. '.', '/' 각각 구분사 기준으로 잘라줌
print(a)
print(b)
print(c)

##합치기: a.join()-글자마다 가운데 /추가해줌.
text='abcde'
print('/'.join(text))

##개수 확인하기: count(a) -a 에 들어간 문자의 갯수를 세줌
text= 'abcde ABC ABC'
print(text.count('a'))
print(text.count('A'))
print(text.count('1'))

##제거하기: strip(a)-양쪽, lstrip(a)-왼쪽, rstrip(a)-오른쪽, 공백(빈칸지워줌) but 문자 중간에 있는 것은 제거불가.
text='  abcde  '
print(text.strip())
print(text.lstrip())
print(text.rstrip())

##인덱스 찾기: find(a)/ rfind(a) -얘네는 없는거 찾으라고 시키면 -1 리턴/ index(a) / rindex(a)-얘네는 에러!
text = 'ABC ABC'
print(text.find('A')) #왼쪽
print(text.rfind('A')) #오른쪽
print(text.index('A')) #왼쪽
print(text.rindex('A')) #오른쪽

##확인하기: isalpha()/ isdigit()/ isalnum()/ isupper()/ islower()-불리언으로 답을 해줌
text1='ABCabc123'
text2='123' 
text3='Abc'
text4='abc'

print(text1.isalpha()) #알파벳으로만 이루어져있는지 확인
print(text1.isdigit()) #숫자로만 이루어져?
print(text1.isalnum()) #숫자와 알파벳의 조합?
print(text1.isupper()) #대문자로?
print(text1.islower()) #소문자로?

##대/소문자 만들기 : upper()/ lower()
text='ABCabc'
print(text.upper())
print(text.lower())


##10. 0codnrl: zfill() - ()안에 들어간 숫자만큼으로 앞에 0 채워줌.
y='2025'
m='2'
d='13'
print(y.zfill(4))
print(m.zfill(2))
print(d.zfill(4))