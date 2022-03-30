# better 04
# 복잡한 표현식 대신 헬퍼 함수를 작성하자

# 예제 : url에서 쿼리 문자열을 디코드 해야 한다면. 각 쿼리 문자열 파라미터는 정수 값을 표현함
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

# 파라미터가 없거나 비어 있으면 기본값으로 0을 할당하게 한다. 이 로직은 if가 아닌 boolean 표현식으로 처리할 수 있음
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)

# if/else 조건식을 이용하면 코드를 짧게 유지하면서도 더 명확하게 표현할 수 있음
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

#하지만 이 로직을 반복해서 써야 한다면 헬퍼 함수를 만드는게 좋음

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')

# 표현식이 복잡해지기 전에 작은 조각으로 분할하고 로직을 헬퍼 함수로 옮겨야 함
# 무조건 짧은 코드보다는 가독성을 선택해야 함