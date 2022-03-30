# better 06
# 한 슬라이스에서 start, end, stride를 함께 쓰지 말자. 굳이 사용해야 한다면 양수값을 사용하고 start, end는 생략한다
# somelist[start:end:stride]처럼 슬라이스의 스트라이드(간격)을 설정하는 문법이 있음

# 홀수와 짝수 인덱스를 그룹으로 묶기
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

# 하지만 종종 버그를 만들어 냄. 바이트 문자열을 역순으로 만들때 -1 stride를 하는데
# 아래 코드는 바이트 문자열이나 아스키 문자에는 잘 동작하지만 URT-8 바이트 문자열로 인코드된 유니코드 문자에는 동작하지 않음
x = b'mongoose'
y = x[::-1]
print(y)
