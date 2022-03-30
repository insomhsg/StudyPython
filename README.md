# StudyPython

Check python version
```
python --version
```
 
## Style guide
1. Whitespace
   - 탭이 아닌 스페이스(4개) 사용
   - 한줄의 문자 길이가 79자 이하
   - 함수와 클래스는 빈 줄 두 개로 구분
   - 클래스에서 메서드는 빈 줄 하나로 구분
   - 리스트 인덱스, 함수 호출, 키워드 인수 할당에는 스페이스 사용하지 않음 
   - 변수 할당 앞뒤에 스페이스를 하나만 사용

2. naming
   - 함수, 변수, 속성은 ```lowercase_underscore```
   - proteced 속성은 ```_leading_underscore```
   - private 속성은  ```__double_leading_underscore```
   - 클래스와 예외는 ```CapitalizedWord```
   - 모듈 수준 상수는 ```ALL_CAPS```
   - 클래스의 인스턴스 메서드에서 첫번째 파라미터(해당 객체를 참조)는 ```self```로 지정
   - 클래스 메서드에서 첫 번째 파라미터(해당 클래스를 참조)는 ```cls```로 지정

3. 표현식과 문장 
   - 긍정 표현식의 부정(if not a is b) 대신에 인라인 부정(if a is not b)을 사용 
   - 길이를 확인(if len(somelist) == 0) 하여 빈값([], '')을 확인하지 않는다. if not somelist를 사용하고 빈값은 암시적으로 False가 된다고 가정한다
   - 한줄로 된 if문, for, while 루프, except 복합문을 쓰지 않고 여러 줄로 나눠서 명료하게 작성
   - 항상 파일의 맨뒤에 import 문을 놓음
   - import 시 상대 경로로 된 이름을 사용하지 않음 
     - 예를 들어 import foo -> from bar import foo
   - 상대적인 임포트를 해야 한다면 명시적인 구문을 써서 from . import foo
   - import 시 표준 라이브러리 모듈, 서드파티 모듈, 자신이 만든 모듈 섹션 순으로 구별. 하위 섹션은 알파벳 순서로 임포트

