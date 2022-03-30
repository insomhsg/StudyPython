# better 07
# map, filter 대신 list comprehension (함축 표현식)을 사용하자

# 만약 리스트의 각 숫자의 제곱을 계산한다고 했을 때
from asyncio import events


a = [1,2,3,4,5,6,7,8,9,10]
squars = [x**2 for x in a]
print(squars)

# map을 쓸 경우 lambda 함수를 생성해야 해서 깔끔하지 않음
squars = map(lambda x:x**2, a)

# list comprehension으로 변경 시 추가 조건도 넣을 수 있음
# 2의 배수만 제곱한다고 하면 
even_squars = [x**2 for x in a if x % 2 == 0]
print(even_squars)

# 이걸 filter+map으로 구현하면 복잡하다
alt = map(lambda x : x**2, filter(lambda x : x % 2 == 0, a))
assert even_squars == list(alt)

# better 08
# list comperehension에서 표현식을 두 개 넘게 쓰지 말자

# 다음은 for 표현식 두 개를 사용한 리스트 컴프리헨션인데 이 표현식은 왼쪽에서 오른쪽 순서로 실행됨
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

# better 09
# comprehenstion이 클 때는 제너레이터 표현식을 고려하자
# list comprehension은 입력 시퀀스에 있는 각 값별로 아이템을 하나씩 담은 새 리스트를 통째로 생성하여 메모리를 많이 소모한다

# 아래 예제에서는 각 줄의 길이만큼 메모리가 필요하다 
value = [len(x) for x in open('/tmp/my_file.txt')]
print(value)

# 리스트 컴프리헨션과 제너레이터를 일반화한 제너레이터 표현식을 제공함 
# 제너레이터 표현식은 실행될 때 출력 시퀀스를 모두 구체화하지 않음
# 표현식에서 한 번에 한 아이템을 내주는 iterator임

it = (len(x) for x in open('/tmp/my_file.txt'))
print(it)

print(next(it))

# 다른 제너레이터 표현식과 함께 사용할 수 있는 것이 장점
roots = ((x, x**0.5) for x in it)
print(next(roots))