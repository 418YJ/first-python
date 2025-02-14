a=int(input('나이를 입력하세요.'))
print(a)
print(a+a)

print(round(3.89,1))
print(pow(3,2))

x,y=divmod(7,2)
print(x) #몫
print(y) #나머지

#최대값
print(max([7,5,1,3]))

#최소값
print(min(7,5,1,3))

#집합도 되고 그냥해도됨, 합은 집합만됨! 배열이라고 해야할지 집합이라고 해야할지 모르겠음.

#합
print(sum([7,5,1,3]))

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


